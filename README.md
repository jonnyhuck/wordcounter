# Word Counter

A simple script to facilitate the production of word clouds to identify themes in text data.

## Installation:
Word counter is just a simple Python script that depends on the [NLTK](http://www.nltk.org/) library for **Natural Language Processing**, which can be installed with either:

```bash
pip install nltk
```

or

```bash
conda install -conda-forge nltk
```

Once installed, you need to open the python interpreter and run these two commands one after the other:

```python
import nltk
nltk.download()
```

This opens a graphical installer. You need to use it to download:

* The WordNet Corpus
* The Punkt Tokenizer
* The Averaged Perceptron Tagger

That should be everything that you need to run the tool.

## Usage:

Normal usage:

```
python wordcounter.py -i path/to/input/file.txt
```

Quiet usage:

```
python wordcounter.py -i path/to/input/file.txt -q
```

Help:

```
python wordcounter.py -h
```

## Outputs:

The script outputs two files:

* `noun_counts.csv`: a report with each noun and its number of occurrences (minimum 2)
* `word_cloud.txt`: a text file to produce a word cloud of the nouns, for use with an online word cloud generator (normally you just need to paste the text in, or upload the file).





