import pandas as pd
import numpy as np
import os
import urllib.request
import gzip
import shutil

from tqdm import tqdm

def download_urdu_corpus(filename="urdu-tagged-corpus"):
    """
    Download and extract the Urdu tagged corpus if it doesn't exist locally.
    
    Args:
        filename (str): The name of the extracted corpus file
    
    Returns:
        str: The path to the corpus file
    """
    if os.path.exists(filename):
        print(f"Corpus file '{filename}' already exists locally. Skipping download.")
        return filename
    
    url = "https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11858/00-097C-0000-0023-65A9-5/urdu-tagged-corpus.gz"
    gz_filename = "urdu-tagged-corpus.gz"
    
    try:
        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, gz_filename)
        print(f"Downloaded {gz_filename}")

        # Extract the gzip file
        print(f"Extracting {gz_filename}...")
        with gzip.open(gz_filename, 'rb') as f_in:
            with open(filename, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"Extracted to {filename}")

        # Remove the .gz file after extraction
        os.remove(gz_filename)
        print(f"Removed {gz_filename}")
        
    except Exception as e:
        print(f"Error downloading or extracting corpus: {e}")
        if os.path.exists(gz_filename):
            os.remove(gz_filename)
        raise
    
    return filename


def parse_tag_file(filepath,max_lines=1000000):
    sentences = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in tqdm(file,total=max_lines):
            line = line.strip()
            if not line:
                continue  # skip empty lines
            tokens = []
            for item in line.split():
                if '|' in item:
                    word, tag = item.rsplit('|', 1)
                    tokens.append((word, tag))
            if tokens:
                sentences.append(tokens)
            
            if len(sentences)==max_lines:
                break
        
    return sentences


# Download corpus if not available locally
# corpus_filename = "urdu-tagged-corpus"
corpus_filename = "testing"
filepath = download_urdu_corpus(corpus_filename)

sentences = parse_tag_file(filepath, 
                           max_lines=1000
                          )

# Example
print(f"Total sentences: {len(sentences)}")
print("First 5 sentences:", sentences[0:5])
