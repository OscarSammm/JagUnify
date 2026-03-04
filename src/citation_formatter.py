import re
#Validates and formats the response for the UI and ensures inline citations match the source list and handles refusals.
def format_citations(response):

    #Handle Refusal Case
    # If the response is empty or indicates no information found
    refusal_msg = "I cannot find supporting information in the indexed TAMUSA documents."
    
    if not response or not response.source_nodes:
        return {
            "answer": refusal_msg,
            "sources": []
        }

    answer_text = response.response
    source_nodes = response.source_nodes
    formatted_sources = []

    #Extract and Format Sources
    for i, node in enumerate(source_nodes):
        index = i + 1
        url = node.metadata.get('source_url', 'https://www.tamusa.edu')
        
        #Grab a small snippet of the text used (first 150 chars)
        snippet = node.get_content()[:150].strip().replace("\n", " ") + "..."
        
        formatted_sources.append({
            "id": index,
            "url": url,
            "snippet": snippet
        })

    #Final Verification
    # Ensure the answer actually contains citation brackets [1]
    # If the LLM forgot them, we return the refusal to stay grounded
    if "[" not in answer_text and "]" not in answer_text:
        # Check if the text itself says it doesn't know
        if "sorry" in answer_text.lower() or "cannot find" in answer_text.lower():
            return {"answer": refusal_msg, "sources": []}

    return {
        "answer": answer_text,
        "sources": formatted_sources
    }

def print_display(formatted_output):
    print(f"\nResponse: {formatted_output['answer']}")
    
    if formatted_output['sources']:
        print("\n--- SOURCES USED ---")
        for src in formatted_output['sources']:
            print(f"[{src['id']}] {src['url']}")
            print(f"    Preview: {src['snippet']}\n")
    else:
        print("\n(No sources verified for this response)")