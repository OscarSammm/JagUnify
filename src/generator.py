import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import os
from llama_index.core import PromptTemplate, Settings
from llama_index.core.query_engine import CitationQueryEngine
from llama_index.llms.openai import OpenAI
from retrieval import get_retriever

# Sets up the engine that turns retrieved chunks into a final answer with citations
def jag_query_engine(index):

    # FIX 1: Use gpt-4o-mini to stop the stuttering/looping bug
    Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.1)

    # Custom prompt template for strict grounding
    qa_prompt_tmpl_str = (
        "You are the JagUnify Assistant, an official resource for Texas A&M University-San Antonio.\n"
        "Context information is provided below from campus documents.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Instructions:\n"
        "1. Answer the query using ONLY the context provided.\n"
        "2. Use inline citations in the format [1], [2], etc.\n"
        "3. If the answer is not contained in the context, strictly say: "
        "'I am sorry, but I cannot find supporting information in the indexed TAMUSA documents.'\n\n"
        "Query: {query_str}\n"
        "Answer: "
    )

    qa_prompt = PromptTemplate(template=qa_prompt_tmpl_str)

    # Initialize the Citation engine
    query_engine = CitationQueryEngine.from_args(
        index=index,
        similarity_top_k=3,
        citation_chunk_size=512,
    )

    query_engine.update_prompts({"response_synthesizer:text_qa_template": qa_prompt})

    return query_engine

if __name__ == "__main__":
    from retrieval import get_retriever
    from citation_formatter import format_citations, print_display
    
    # 1. Load the existing storage
    # (Only use build_vector_store_index() if you have deleted the /storage folder)
    retriever_obj = get_retriever(index=None)
    index = retriever_obj._index
    
    # 2. Initialize the grounded engine
    engine = jag_query_engine(index)
    
    # --- TEST 1: Grounded Policy Question ---
    print("TEST 1: GROUNDED TAMUSA INQUIRY")
    
    query_1 = "Can you give me the degree plan of study for the Computer Science major at TAMUSA?"
    response_1 = engine.query(query_1)
    
    # Pass raw response through the Citation Layer
    final_output_1 = format_citations(response_1)
    print_display(final_output_1)

    # --- TEST 2: Out-of-Scope (Refusal) ---
    print("TEST 2: OUT-OF-SCOPE REFUSAL")
    
    query_2 = "Lowkenuinely what should i eat tomorrow?"
    response_2 = engine.query(query_2)
    
    # Pass through Citation Layer to ensure it triggers the mandatory refusal message
    final_output_2 = format_citations(response_2)
    print_display(final_output_2)