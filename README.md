#Word Counter

A simple script 

##Installation:
Word counter is just a Python script, so does not need installing per se. It does, however, depend upon the [NLTK](http://www.nltk.org/) library, which can be installed with:

```
sudo pip install nltk
```

Once installed, you need to run this command in the interpreter:

```
>>> import nltk
>>> nltk.download()
```

and then download:

* The WordNet Corpus
* The Punkt Tokenizer
* The Averaged Perceptron Tagger

That should be everything that you need to run it.

##Usage:

Normal usage:

```
python wordcloud_generator.py -i path/to/input/file.txt
```

Quiet:

```
python wordcloud_generator.py -i path/to/input/file.txt -q
```

Help:

```
python wordcloud_generator.py -h
```






