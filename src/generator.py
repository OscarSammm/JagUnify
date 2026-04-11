import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*urllib3.*")
from llama_index.core import PromptTemplate, Settings
from llama_index.core.query_engine import CitationQueryEngine
from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage, MessageRole
from retrieval import load_index

CANDIDATE_K = 20  # Initial retrieval pool for the re-ranker to select from
TOP_K = 7         # Final chunks passed to the LLM after re-ranking

# Sets up the engine that turns retrieved chunks into a final answer with citations
def jag_query_engine(index):

    Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0)

    # Custom prompt template for strict grounding
    qa_prompt_tmpl_str = (
        "You are the JagUnify Assistant, an academic advisor chatbot for Texas A&M University-San Antonio.\n"
        "Context information is provided below from the official TAMUSA academic catalog.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Instructions:\n"
        "1. Answer the query using ONLY the context provided.\n"
        "2. Every sentence that uses information from the context MUST include an inline citation in the format [1], [2], etc. Do not write any factual sentence without a citation.\n"
        "3. Do NOT include any URLs or hyperlinks in your answer. Reference sources using citation numbers only.\n"
        "4. If the answer is not contained in the context, strictly say: "
        "'I am sorry, but I cannot find supporting information in the indexed TAMUSA documents.'\n\n"
        "Query: {query_str}\n"
        "Answer: "
    )

    qa_prompt = PromptTemplate(template=qa_prompt_tmpl_str)

    # Re-ranker: scores each (question, chunk) pair together so the best chunks
    # reach the LLM regardless of surface-level wording overlap between doc types
    reranker = SentenceTransformerRerank(
        model="cross-encoder/ms-marco-MiniLM-L-12-v2",
        top_n=TOP_K,
    )

    query_engine = CitationQueryEngine.from_args(
        index=index,
        similarity_top_k=CANDIDATE_K,
        citation_chunk_size=1024,
        node_postprocessors=[reranker],
    )

    query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_prompt})

    return query_engine


# Rewrites the latest question as a standalone question given prior conversation turns.
# history is a list of {"role": "human"|"bot", "text": "..."} dicts.
# Returns the condensed question string (or original question if no history).
def condense_question(history: list, question: str) -> str:
    if not history:
        return question

    llm = OpenAI(model="gpt-4o-mini", temperature=0)

    convo_lines = []
    for turn in history:
        role = "User" if turn.get("role") == "human" else "Assistant"
        convo_lines.append(f"{role}: {turn.get('text', '')}")
    convo_text = "\n".join(convo_lines)

    system_msg = ChatMessage(
        role=MessageRole.SYSTEM,
        content=(
            "Given the conversation history and a follow-up question, "
            "rewrite the follow-up question as a fully self-contained standalone question. "
            "Do not answer the question — only rewrite it. "
            "If the follow-up is already standalone, return it unchanged."
        ),
    )
    user_msg = ChatMessage(
        role=MessageRole.USER,
        content=f"Conversation:\n{convo_text}\n\nFollow-up question: {question}\n\nStandalone question:",
    )

    response = llm.chat([system_msg, user_msg])
    return response.message.content.strip()

