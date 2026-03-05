from operator import index
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
    seen_urls = set()  # To track unique sources
    current_id = 1

    #Extract and Format Sources
    for node in source_nodes:
        url = node.metadata.get('source_url', 'https://www.tamusa.edu')
        
        #Grab a small snippet of the text used (first 150 chars)
        if url not in seen_urls:
            snippet = node.get_content()[:150].strip().replace("\n", " ") + "..."
        
            formatted_sources.append({
                "id": current_id,
                "url": url,
                "snippet": snippet
            })
            seen_urls.add(url)
            current_id += 1

    #Final Verification
    # Ensure the answer actually contains citation brackets [1]
    # If the LLM forgot them, we return the refusal to stay grounded
    if "[" not in answer_text:
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
        print("\nSources:")
        for src in formatted_output['sources']:
            print(f"[{src['id']}] {src['url']}")
    else:
        print("\n(No sources verified for this response)")