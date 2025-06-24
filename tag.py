import argparse
import dill

# Load the HMM tagger
with open("urdu_hmm_tagger.pkl", "rb") as f:
    tagger = dill.load(f)


def tag_urdu_sentence(sentence):
    # Simple whitespace-based tokenizer
    tokens = sentence.strip().split()
    if not tokens:
        return []

    tagged = tagger.tag(tokens)
    return tagged


def print_tagged_output(tagged_sentence):
    """Print the tagged output in a nicely formatted way"""
    if not tagged_sentence:
        print("No words to tag.")
        return
    
    print("\n" + "="*60)
    print("              URDU POS TAGGING RESULTS")
    print("="*60)
    print(f"{'Word':<20} {'POS Tag':<15}")
    print("-"*35)
    
    for word, tag in tagged_sentence:
        print(f"{word:<20} {tag:<15}")
    
    print("-"*35)
    print(f"Total words tagged: {len(tagged_sentence)}")
    print("="*60)


def main():
    parser = argparse.ArgumentParser(description='Tag Urdu sentence with Part-of-Speech tags using HMM')
    parser.add_argument('sentence', type=str, help='Urdu sentence to be tagged')
    
    args = parser.parse_args()
    
    print(f"\nInput sentence: {args.sentence}")
    
    tagged_result = tag_urdu_sentence(args.sentence)
    print_tagged_output(tagged_result)


if __name__ == "__main__":
    main()
