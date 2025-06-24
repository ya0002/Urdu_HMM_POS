
--, Mohammad Yusuf Jamal, [Your Matriculation Number Here]

PoS Tagger for Urdu Language using HMM

# Project description

This project implements a **Hidden Markov Model (HMM)-based Part-of-Speech (PoS) tagger** for the Urdu language. It uses statistical modeling to assign the most probable PoS tags to words in Urdu sentences, based on a tagged corpus. The system learns transition probabilities (between PoS tags) and emission probabilities (word given a tag) during training, and then applies the Viterbi algorithm for decoding.

Accuracy of tagger: 90.10 %

The translated corpus is in `translated.txt`.

The corpus used is:
**"A Tagged Corpus and a Tagger for Urdu"**  
*Authors:* Bushra Jawaid, Amir Kamran, Ondřej Bojar  
*Institution:* Charles University in Prague, Faculty of Mathematics and Physics, Institute of Formal and Applied Linguistics

It has 5,464,575 sentences.

In this corpus each token (word or punctuation mark) is followed by a PoS tag, separated by a vertical bar (|). Each line represents a sentence.

Example: 

Each line is made of multiple `PoS|word`. (Urdu is written from right)

```
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

  *(The complete tagset is documented and handled in the code.)*

# Used AI

ChatGPT was used in the development process for:

* Designing the HMM-based approach
* Understanding how to train transition and emission probabilities
* Explaining and implementing the Viterbi decoding algorithm
* Writing documentation such as this README

**Prompts used:**

* "How do I implement a PoS tagger using HMM in Python?"
* "Explain the Viterbi algorithm with Urdu PoS tagging as an example."
* "Help me write a README for a PoS tagger based on an HMM model."

# Implementation of the Requests

| Requirement                               | Implementation Details                                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------ |
| Description of sentences, words, PoS-tags | See `Alternative Language` section and inline code comments                          |
| Tagged Urdu corpus usage                  | Loaded via `load_corpus()` in `main.py`                                              |
| HMM Model implementation                  | `train_hmm()` for transition/emission probabilities, Viterbi decoding in `viterbi()` |
| Output interpretation                     | Printed as tagged sequences per sentence                                             |
| Completeness                              | Modular code with clear preprocessing, training, and testing phases                  |

---


