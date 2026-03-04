import os
import re
from llama_index.core import Document

#Extracts the source URL from the markdown file header
def extract_source_url(file_path):
    try:    
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            match = re.search(r'SOURCE:\s*(https?://\S+)', content)
            if match:
                return match.group(1).strip()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return "Unknown Source"

#loads all markdown files and attatches metadata
def load_tamusa_data(directory_path):
    documents = []
    for root, dirs, files in os.walk(directory_path):
        category = os.path.basename(root)

        #We walk through the subfolders: /catalog and /main_site
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                #Extract the URL from the file header
                source_url = extract_source_url(file_path)

                #Read the content of the file while skipping the first line
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()


                    #Create a LLamaIndex Document with the metadata
                    #This metadata is what allows for "verifiable citations"
                    doc = Document(text=content, metadata={"file_name": file, "category": category, "source_url": source_url}, excluded_llm_metadata_keys=["file_name"]) #so we dont confuse the AI with filenames
                    documents.append(doc)
    return documents

if __name__ == "__main__":
    #We test the ingestion from our local folder
    directory_path = './docs'
    # documents = load_tamusa_data(directory_path)