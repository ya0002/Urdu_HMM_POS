
--, Mohammad Yusuf Jamal, [Your Matriculation Number Here]

# PoS Tagger for Urdu Language using HMM

# Project description

This project implements a **Hidden Markov Model (HMM)-based Part-of-Speech (PoS) tagger** for the Urdu language. It uses statistical modeling to assign the most probable PoS tags to words in Urdu sentences, based on a tagged corpus. The system learns transition probabilities (between PoS tags) and emission probabilities (word given a tag) during training, and then applies the Viterbi algorithm for decoding.

Accuracy of tagger with ~5.4 million sentences on a 80:20 split: 90.10 %

The translated corpus is in `translated.txt`.

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


<!-- # Implementation of the Requests -->