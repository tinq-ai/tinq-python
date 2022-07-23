# Tinq.ai Python Library

![Tinq.ai logo](https://res.cloudinary.com/tinq-ai/image/upload/v1642011382/website/tinq-logo-with-bee_tkaj18.svg)

A Python wrapper for the Tinq.ai API - an easy-to-use text analysis and natural language processing toolkit.

## Documentation

Find the full API documentation [here](https://developers.tinq.ai/)

## Requirements

Python 3.7 or higher

## Installation
Install the package with:

```sh

pip install tinq

```

## Usage

### Table of Contents

- [Authentication](#authentication)
- [Rewriter](#rewriter)
- [Summarizer](#summarizer)
- [Classifier](#classifier)
- [Article Extractor](#article-extractor)
- [Sentiment analysis](#sentiment-analysis)
- [Plagiarism Checker](#plagiarism-checker)
  
> Please note that all methods return associative arrays. Responses can be found in the developer documentation [here](https://developers.tinq.ai/).

### Authentication

Get the API key for your project in Tinq.ai and then instantiate a new client.

```python
from tinq import Tinq

tinq = Tinq(api_key='<api-key>')
```

Alternatively, set the API key and your username in an environment variable named `TINQ_API_KEY` & `TINQ_USERNAME`, respectively.

```python

from tinq import Tinq

tinq = Tinq()

```

### Rewriter
Rewrites/paraphrases a given text.

`text` is the piece of content that you'd like to rewrite.
list of accepted parameters is available [here](https://developers.tinq.ai/reference/rewriter).
  
```python
text = "The process of learning a new piece of music is fantastic. You start from nothing, practise, improve, and finally get the fruits of your hard work, as farmers do during the harvest time."
rewritten = tinq.rewrite(text)

```

### Summarizer
Summarizes a given text.

`text` is the piece of content that you'd like to summarize.
list of accepted parameters is available [here](https://developers.tinq.ai/reference/summarizer).
  
```python

text = "Bernal’s case study is Tullis Mason, a chap who sports “three-quarter length shorts” even in a lab coat. Matson runs an artificial insemination company for racehorses from his family’s farm in Shropshire, England. However, on the side, he is also planning to save the animal kingdom by building the biggest biobank of animal cells in Europe. It’s not always a dignified business, with Bernal describing Mason hooking an elephant penis into a device that looks like “a huge condom,” but the science and the ethics her article explores are fascinating. We may not be about to bring dinosaurs back to life, but with help from biobanking, life already on this planet might still find a way."
summary = tinq.summarize(text)

```


### Classifier
Classifies a given text, according to a classifier that you specify

`$text` is the piece of content that you'd like to summarize.
`$classifier` is the piece of content that you'd like to summarize.
`$params` is optional, a list of accepted parameters is available [here](https://developers.tinq.ai/reference/classifier).
  
```python

text = "Hi, I need help with my website."
classifier = "fjew833" # ID of your classifier on Tinq.ai
classified = tinq.classify(text=text, classifier=classifier)

```

### Article Extractor
Extractor API is a feature-rich API and online application that handles all of the tedious work and problems associated with clean text extraction.

`url` URL from which you want to extract an article.
list of accepted parameters is available [here](https://developers.tinq.ai/reference/article-extractor).
  
```python

url = "https://longreads.com/2021/08/19/bringing-species-back-from-the-brink/"
extracted = tinq.extract_article(url=url)

```


### Sentiment Analysis
Performs sentiment analysis operations for a given string.

`text` is the piece of content that you'd like to summarize.
list of accepted parameters is available [here](https://developers.tinq.ai/reference/sentiment-analysis).
  
```python

text = "I really like you."
sentimentAnalysis = tinq.sentiments(text=text)

```

### Plagiarism Checker
Checks for plagiarism and finds online sources for a given content.

`text` is the piece of content that you'd like to summarize.
list of accepted parameters is available [here](https://developers.tinq.ai/reference/plagiarism-checker).
  
```python

text = "Bernal’s case study is Tullis Mason, a chap who sports “three-quarter length shorts” even in a lab coat. Matson runs an artificial insemination company for racehorses from his family’s farm in Shropshire, England."
checkPlagiarism = tinq.check_plagiarism(text=text)

```

## Contributing


Bug reports and pull requests are welcome on GitHub at https://github.com/tinq-ai/tinq-python.
  

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).