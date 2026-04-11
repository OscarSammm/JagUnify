import os
import re
import json
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

#loads all markdown files and attatches metadata (legacy — kept for reference)
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

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    #Strip nav boilerplate — keep only content from the first heading onwards
                    heading_match = re.search(r'^#{1,6}\s', content, re.MULTILINE)
                    if heading_match:
                        content = content[heading_match.start():]

                    #Create a LLamaIndex Document with the metadata
                    #This metadata is what allows for "verifiable citations"
                    doc = Document(text=content, metadata={"file_name": file, "category": category, "source_url": source_url}, excluded_llm_metadata_keys=["file_name"]) #so we dont confuse the AI with filenames
                    documents.append(doc)
    return documents

# Loads structured JSONL data from the tech department.
# catalog.jsonl is the combined file (programs + courses + information).
# Each record's full_body is used as the document text; source_url, title,
# and record_type are stored as metadata for citations.
def load_jsonl_data(jsonl_path):
    documents = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)

            text = rec.get('full_body', '').strip()
            if not text:
                continue

            metadata = {
                "source_url": str(rec.get('source_url', 'https://www.tamusa.edu')),
                "title": rec.get('title', ''),
                "record_type": rec.get('record_type', ''),
            }

            doc = Document(
                text=text,
                metadata=metadata,
                excluded_llm_metadata_keys=["record_type"],
            )
            documents.append(doc)

    print(f"Loaded {len(documents)} documents from {jsonl_path}")
    return documents

if __name__ == "__main__":
    jsonl_path = '../data/techdep_data/catalog.jsonl'
    docs = load_jsonl_data(jsonl_path)
    print(f"Sample: {docs[0].metadata}")