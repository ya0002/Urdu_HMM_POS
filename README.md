
--, Mohammad Yusuf Jamal, 12501464

# PoS Tagger for Urdu Language using HMM

# Project description

This project implements a **Hidden Markov Model (HMM)-based Part-of-Speech (PoS) tagger** for the Urdu language. It uses statistical modeling to assign the most probable PoS tags to words in Urdu sentences, based on a tagged corpus. The system learns transition probabilities (between PoS tags) and emission probabilities (word given a tag) during training, and then applies the Viterbi algorithm for decoding.

Accuracy of tagger with ~5.4 million sentences on a 80:20 split: `90.10 %`

The translated corpus is in `translated.txt`. It has ~121 K sentences.

### Corpus used
The corpus used is:
**"A Tagged Corpus and a Tagger for Urdu"**  
*Authors:* Bushra Jawaid, Amir Kamran, Ondřej Bojar  
*Institution:* Charles University in Prague, Faculty of Mathematics and Physics, Institute of Formal and Applied Linguistics

[Homepage of the dataset. I used urdu-tagged-corpus.gz](https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0023-65A9-5#)

Number of sentences: 5,464,575 sentences

Vocabulary: ~582,795 unique word types

Annotation: Automatically tagged with POS tags using an ensemble of three taggers

In this corpus each token (word or punctuation mark) is followed by a PoS tag, separated by a vertical bar (|). Each line represents a sentence.

Example: 

Each line is made of multiple `PoS|word`. (Urdu is written from right)

```haskell
بلال|PN بھائی|PN ،|PM ہم|PP آپ|PP کی|P محنت|NN کے|P معترف|NN اور|CC قائل|ADJ ہیں|VB ۔|SM
```



# Prerequisites

- Python >= 3.11
- pip install nltk dill

# Installation

1. Clone the repository or extract the ZIP archive.
2. Navigate to the project folder in the terminal.
3. Install dependencies using:

   ```bash
   pip install -r requirements.txt
   ```
4. extract `urdu_hmm_tagger.zip` to get `urdu_hmm_tagger.pkl`.



# Basic Usage

To run the PoS tagger:


1. With a custom trained model, will automatically download the corpus by the name `urdu-tagged-corpus`
    ```bash
    python train_n_tag.py --max_lines 2000 --train-split 0.75 --sentence "میں اردو سیکھ رہا ہوں"
    ```


2. On a model trained with 5.4 million sentences from `urdu_hmm_tagger.pkl`
    ```bash
    python tag.py "{sentence}"
    ``` 

    For example `python tag.py "دو ہزار سال پرانی پینٹگ"` 


# Alternative Language

**Urdu Language Description**

Urdu is a language spoken in the northern regions of the Indian subcontinent.

It uses the Persian script and has linguistic influences from Persian as well as various Indian languages.

Urdu is written from right to left. 

* **What is a sentence?**
  
  A sentence in Urdu is a complete grammatical unit, typically ending with a punctuation mark like (۔). It includes a subject, predicate, and can also include modifiers, objects, and conjunctions.

* **Tagset**

  The dataset uses a unified part-of-speech tagset known as Sajjad’s Tagset, which is a consolidation of tagsets from:

  1. CRULP (Center for Research in Urdu Language Processing)

  2. HUM Analyzer (Humayoun's morphological analyzer)

  3. SH Parser (Shallow Parser by IIIT Hyderabad)


  | Tag      | Description                                                                                         |
  | -------- | --------------------------------------------------------------------------------------------------- |
  | **A**    | Possibly *Adjective particle* or *Affix* (rare; unclear from paper)                                 |
  | **AA**   | **Auxiliary verb A** – e.g., *hai, tha* (used for tense/aspect/mood)                                |
  | **AD**   | **Demonstrative pronoun** or **relative pronoun** (e.g., *jo, ye, vo*)                              |
  | **ADJ**  | **Adjective**                                                                                       |
  | **ADV**  | **Adverb**                                                                                          |
  | **AKP**  | **Interrogative pronoun** – used for asking questions (e.g., *kaun, kya*)                           |
  | **AP**   | Likely **pronoun** (ambiguous in source; possibly *relative* or *interrogative*)                    |
  | **CA**   | **Cardinal number** – e.g., *ek, do, 3*                                                             |
  | **CC**   | **Coordinating conjunction** – e.g., *aur, lekin*                                                   |
  | **DATE** | **Date/time expression**                                                                            |
  | **EXP**  | **Expression** or **symbol**, e.g., punctuation, emoticons, or typographic characters               |
  | **FR**   | **Foreign word** – non-Urdu terms used in text                                                      |
  | **G**    | **Possessive pronoun**, e.g., *mera, tumhara*                                                       |
  | **GR**   | **Reflexive possessive pronoun**, e.g., *apna*                                                      |
  | **I**    | **Particle**, often uninflected words like *to, bhi*                                                |
  | **INT**  | **Interjection**, e.g., *wah, arey*                                                                 |
  | **KD**   | Another **interrogative pronoun** (used interchangeably with AKP/KP)                                |
  | **KER**  | **Postposition marker** – e.g., *ke, ka* (part of genitive constructions)                           |
  | **KP**   | Another form of **interrogative pronoun**                                                           |
  | **MUL**  | **Multi-word verb expression**, e.g., *chala gaya, uth kar gaya*                                    |
  | **NEG**  | **Negation**, e.g., *nahin, na*                                                                     |
  | **NN**   | **Common noun**, e.g., *kitab, admi*                                                                |
  | **N**    | Possibly **noun** (general or undefined class)                                                      |
  | **OR**   | **Ordinal number**, e.g., *pehla, doosra*                                                           |
  | **P**    | **Particle** or **complementizer**, e.g., *ki, ke liye*                                             |
  | **PD**   | **Demonstrative pronoun**, e.g., *yeh, woh*                                                         |
  | **PM**   | **Punctuation mark**, often matched to symbols like commas, periods, etc.                           |
  | **PN**   | **Proper noun**, e.g., *Ali, Pakistan*                                                              |
  | **PP**   | **Personal pronoun**, e.g., *main, tu, wo*                                                          |
  | **Q**    | **Indefinite/quantifier pronoun**, e.g., *kuch, sab, koi*                                           |
  | **QF**   | Likely **quantifier function word** or a **fine-grained quantifier** (not fully explained in paper) |
  | **QW**   | **Question word**, e.g., *kya, kaun, kab*                                                           |
  | **RD**   | **Relative determiner**, e.g., *jo*                                                                 |
  | **REP**  | **Repetition marker**, for emphasis or reduplication (e.g., *baar baar*)                            |
  | **RP**   | **Reflexive pronoun**, e.g., *khud*                                                                 |
  | **SC**   | **Subordinating conjunction**, e.g., *agar, jab, ke*                                                |
  | **SE**   | **Postposition**, e.g., *se, mein, tak*                                                             |
  | **SM**   | **Symbol**, such as mathematical or special characters                                              |
  | **TA**   | **Auxiliary verb T** – another form of auxiliary (used in tense constructions)                      |
  | **U**    | **Uncategorized or unknown class**                                                                  |
  | **UNK**  | **Unknown token** (unrecognized by tagger)                                                          |
  | **VB**   | **Verb**, e.g., *karna, jana*                                                                       |
  | **WALA** | **‘Wala’ participle construction**, e.g., *khilne wala, karne wala*                                 |


* **Used PoS-tags with examples:**

  | Tag | Description        | Example (Urdu) | English Equivalent |
  | --- | ------------------ | -------------- | ------------------ |
  | NN  | Noun               | محنت           | work               |
  | VB  | Verb               | آیاہے          | has come           |
  | PN  | Proper Noun        | بلال           | Bilal              |
  | ADJ | Adjective          | محفوظات        | secure             |
  | ADV | Adverb             | برائے          | for                |
  | PP  | Personal Pronoun   | ہم             | we                 |
  | P   | Preposition        | کا             | of                 |
  | SM  | Sentence Marker    | ۔              | .                  |
  | CC  | Coordinating Conj. | اور            | and                |
  | CA  | Cardinal Number    | اکیس           | twenty-one         |
  | PM  | Punctuation Mark   | ،              | ,                  |
  | NEG | Negation           | نہیں           | not                |

  

# Used AI

ChatGPT was used in the development process for:

* Formatting README to markdown
* Function for downloading the dataset if its not available.

**Prompts used:**

* " Rewrite the following info in Markdown: {raw_text}"
* "Write a function to download the file and extract its content if it's not available in the project root" 

# Output examples

1. `python tag.py "آج موسم بہت خوشگوار ہے"`
  - *Today the weather is very pleasant.*
  - Output: ```[('آج', 'NN'), ('موسم', 'NN'), ('بہت', 'ADV'), ('خوشگوار', 'ADJ'), ('ہے', 'VB')]```

2. `python tag.py "میں کتاب پڑھ رہا ہوں"`
  - *I am reading a book.*
  - Output: `[('میں', 'P'), ('کتاب', 'NN'), ('پڑھ', 'VB'), ('رہا', 'AA'), ('ہوں', 'TA')]`

3. `python tag.py "وہ اسکول جا رہی ہے"`
  - *She is going to school.*
  - Output: `[('وہ', 'PP'), ('اسکول', 'NN'), ('جا', 'VB'), ('رہی', 'AA'), ('ہے', 'TA')]`

4. `python tag.py "ہم کل لاہور جائیں گے"`
  - *We will go to Lahore tomorrow.*
  - Output: `[('ہم', 'PP'), ('کل', 'Q'), ('لاہور', 'PN'), ('جائیں', 'AA'), ('گے', 'TA')]`

5. `python tag.py "کیا آپ چائے پئیں گے؟"`
  - *Will you have tea?*
  - Output: `[('کیا', 'QW'), ('آپ', 'PP'), ('چائے', 'NN'), ('پئیں', 'NN'), ('گے؟', 'NN')]`

6. `python tag.py "میرے والد ڈاکٹر ہیں"`
  - *My father is a doctor.*
  - Output: `[('میرے', 'G'), ('والد', 'NN'), ('ڈاکٹر', 'NN'), ('ہیں', 'VB')]`

7. `python tag.py "بچے پارک میں کھیل رہے ہیں"`
  - *Children are playing in the park.*
  - Output: `[('بچے', 'NN'), ('پارک', 'NN'), ('میں', 'P'), ('کھیل', 'VB'), ('رہے', 'AA'), ('ہیں', 'TA')]`

8. `python tag.py "یہ کتاب بہت دلچسپ ہے"`
  - *This book is very interesting.*
  - Output: `[('یہ', 'PD'), ('کتاب', 'NN'), ('بہت', 'ADV'), ('دلچسپ', 'ADJ'), ('ہے', 'VB')]`

9. `python tag.py "مجھے اردو زبان پسند ہے"`
  - *I like the Urdu language.*
  - Output: `[('مجھے', 'PP'), ('اردو', 'PN'), ('زبان', 'NN'), ('پسند', 'NN'), ('ہے', 'VB')]`

10. `python tag.py "آپ کہاں رہتے ہیں؟"`
   - *Where do you live?*
   - Output: `[('آپ', 'PP'), ('کہاں', 'AKP'), ('رہتے', 'VB'), ('ہیں؟', 'NN')]`


# Implementation of the Requests

This chapter describes the implementation of each project request in the codebase. The project implements a Hidden Markov Model (HMM) based Part-of-Speech tagger for Urdu language with comprehensive functionality.

## 1. Evaluate Tagged Corpus

**Implementation Location:** `train_n_tag.py` - functions `download_urdu_corpus()` and `parse_tag_file()`

**Description:** 
The corpus evaluation is implemented through automated download and parsing mechanisms:

- **Corpus Download:** The `download_urdu_corpus()` function automatically downloads the Urdu tagged corpus from LINDAT repository if not available locally
- **Corpus Parsing:** The `parse_tag_file()` function processes the tagged corpus file, extracting word-tag pairs from each sentence
- **Data Structure:** Each sentence is parsed into a list of tuples `(word, tag)` format
- **Corpus Statistics:** The system reports total sentences processed and provides sample output

**Key Code Components:**
```python
def parse_tag_file(filepath, max_lines=1000000):
    sentences = []
    # Parses each line splitting on '|' delimiter
    # Returns list of sentences with (word, tag) tuples
```

## 2. Split Corpus into Train and Test Sentences

**Implementation Location:** `train_n_tag.py` - main execution section

**Description:**
The corpus splitting functionality provides configurable train/test splits:

- **Configurable Split Ratio:** Uses `--train-split` argument (default: 0.8 for 80/20 split)
- **Random Shuffling:** Implements `random.seed(42)` for reproducible splits
- **Split Calculation:** Calculates split index based on percentage and total sentences
- **Data Separation:** Creates `train_sents` and `test_sents` arrays

**Key Code Components:**
```python
random.seed(42)
random.shuffle(sentences)
train_percentage = args.train_split
split_idx = int(train_percentage * len(sentences))
train_sents = sentences[:split_idx]
test_sents = sentences[split_idx:]
```

## 3. Create HMM PoS-Tagger

**Implementation Location:** `train_n_tag.py` - HMM training section

**Description:**
The HMM tagger creation uses NLTK's Hidden Markov Model implementation:

- **Trainer Initialization:** Uses `HiddenMarkovModelTrainer()` from NLTK
- **Supervised Training:** Trains on labeled corpus using `train_supervised(train_sents)`
- **Model Persistence:** Saves trained model using `dill` serialization
- **Timestamped Output:** Creates uniquely named model files with timestamp

**Key Code Components:**
```python
from nltk.tag.hmm import HiddenMarkovModelTrainer
trainer = HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_sents)
# Saves model with timestamp for versioning
```

## 4. Show Accuracy of the PoS-Tagger

**Implementation Location:** `train_n_tag.py` - evaluation section

**Description:**
Accuracy evaluation is performed on the test set:

- **Built-in Evaluation:** Uses NLTK's `tagger.accuracy(test_sents)` method
- **Percentage Display:** Formats accuracy as percentage with 2 decimal places
- **Test Set Validation:** Evaluates on unseen test data for unbiased accuracy

**Key Code Components:**
```python
accuracy = tagger.accuracy(test_sents)
print(f"Accuracy: {accuracy:.2%}")
```

## 5. Read Another Test

**Implementation Location:** `tag.py` - command line interface and `train_n_tag.py` - sentence argument

**Description:**
The system provides multiple ways to input test sentences:

- **Command Line Input:** `tag.py` accepts sentence as command line argument
- **Training Script Input:** `train_n_tag.py` accepts `--sentence` parameter
- **Default Fallback:** Provides default Urdu sentence if none specified
- **Flexible Input:** Supports any Urdu sentence for testing

**Key Code Components:**
```python
# In tag.py
parser.add_argument('sentence', type=str, help='Urdu sentence to be tagged')

# In train_n_tag.py  
parser.add_argument('--sentence', type=str, help='Urdu sentence to tag')
```

## 6. Output PoS-Tags as List of Tuples

**Implementation Location:** `tag.py` - `tag_urdu_sentence()` and `print_tagged_output()`

**Description:**
The output functionality provides both programmatic and formatted output:

- **Tuple Format:** Returns list of `(word, tag)` tuples from `tag_urdu_sentence()`
- **Formatted Output:** `print_tagged_output()` provides human-readable table format
- **Tokenization:** Simple whitespace-based tokenizer for input processing
- **Error Handling:** Handles empty input gracefully

**Key Code Components:**
```python
def tag_urdu_sentence(sentence):
    tokens = sentence.strip().split()
    tagged = tagger.tag(tokens)
    return tagged  # Returns [(word, tag), ...]

def print_tagged_output(tagged_sentence):
    # Formats output in table format with headers
```

## 7. Command Line Interface (No GUI)

**Implementation Location:** `tag.py` and `train_n_tag.py` - argparse implementations

**Description:**
The project implements comprehensive command-line interfaces:

- **Primary Tagger:** `tag.py` provides direct sentence tagging via CLI
- **Training Interface:** `train_n_tag.py` provides full training pipeline control
- **Argument Parsing:** Uses `argparse` for robust command-line argument handling
- **No GUI Dependency:** Pure command-line operation (note: `app.py` contains GUI but is separate)

**Usage Examples:**
```bash
# Tag a sentence
python tag.py "آج موسم اچھا ہے"

# Train with custom parameters
python train_n_tag.py --max_lines 2000 --train-split 0.75 --sentence "میں اردو سیکھ رہا ہوں"
```

## 8. Python Version Compatibility (>= 3.10)

**Implementation Location:** Throughout the codebase

**Description:**
The implementation uses modern Python features and libraries:

- **Modern Syntax:** Uses f-strings, type hints where applicable
- **Updated Libraries:** `requirements.txt` specifies current library versions
- **Standard Library:** Uses modern argparse, datetime formatting
- **No Legacy Code:** No Python 2.x compatibility concerns

**Dependencies:**
```
nltk==3.9.1      # Natural Language Toolkit
dill==0.3.8      # Enhanced pickling
gradio==5.34.2   # Web interface (optional)
```

## System Architecture

The implementation follows a modular architecture:

1. **Data Layer:** Corpus download and parsing (`download_urdu_corpus`, `parse_tag_file`)
2. **Model Layer:** HMM training and persistence (`HiddenMarkovModelTrainer`)
3. **Application Layer:** Command-line interfaces (`tag.py`, `train_n_tag.py`)
4. **Presentation Layer:** Formatted output and optional web interface

## File Structure Summary

- `train_n_tag.py`: Complete training pipeline with evaluation
- `tag.py`: Production tagging interface
- `app.py`: Optional Gradio web interface
- `requirements.txt`: Dependency specification
- `*.pkl`: Serialized trained models

This implementation provides a complete, production-ready Urdu PoS tagging system that fulfills all project requirements while maintaining code quality and usability.
