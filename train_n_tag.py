import pandas as pd
import numpy as np
import os
import urllib.request
import gzip
import shutil
import random

from tqdm import tqdm

import nltk
from nltk.tag.hmm import HiddenMarkovModelTrainer
import dill

from datetime import datetime

def download_urdu_corpus(filename="urdu-tagged-corpus"):
    """
    Function was generated using GenAI.
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

if __name__ == "__main__":
    # Download corpus if not available locally======
    corpus_filename = "urdu-tagged-corpus"
    filepath = download_urdu_corpus(corpus_filename)
    max_lines=1000
    sentences = parse_tag_file(filepath, max_lines=max_lines)

    # Example
    print(f"Total sentences: {len(sentences)}")
    print("First 5 sentences:", sentences[0:5])


    # split dataset======

    random.seed(42)
    random.shuffle(sentences)
    split_idx = int(0.8 * len(sentences))  ## 80:20 split
    train_sents = sentences[:split_idx]
    test_sents = sentences[split_idx:]


    # Train HMM Tagger======
    trainer = HiddenMarkovModelTrainer()
    tagger = trainer.train_supervised(train_sents)

    # Evaluate
    accuracy = tagger.accuracy(test_sents)
    print(f"Accuracy: {accuracy:.2%}")

    # Format datetime to be Windows filesystem compatible (no colons)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"custom_urdu_hmm_tagger_{max_lines}__{timestamp}.pkl", "wb") as f:
        dill.dump(tagger, f)

    ## tag the sentence
    urdu_sentence = ["آج", "موسم", "اچھا", "ہے"]
    tagged = tagger.tag(urdu_sentence)
    print("Tagged:", tagged)
