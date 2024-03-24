# Analyzing Text Data with Word Clouds and N-grams

This Python script is designed to analyze text data by generating word clouds and extracting n-grams to identify and visualize common patterns within the text. 

## Table of Contents

- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)


## About The Project

The project includes a Python script that reads text data, processes it, and performs two main tasks:
1. **Word Cloud Generation**: Creates a visual word cloud representing the frequency of individual words in the text.
2. **N-grams Extraction**: Identifies and counts the top n-grams (a contiguous sequence of n items from a given sample of text) to analyze common phrases or terms.


## Getting Started

To get a local copy up and running, follow these simple steps.

### Usage

After installing the required packages and running the script, you will see:

A word cloud image popping up, displaying the most common words in your text data.
A list of the top n-grams printed out to the console.
You can modify the n_gram_size and top_n_grams parameters in the script to adjust the size of the n-grams and the number of top n-grams to display.

### Prerequisites

This script requires the following Python libraries:
- `nltk`
- `matplotlib`
- `wordcloud`

You can install these packages using `pip`:

```bash
pip install nltk matplotlib wordcloud

Installation

Clone the repository:
git clone https://github.com/Majid-Dev786/Analyzing-Text-Data-with-Word-Clouds-and-N-grams.git
Navigate to the cloned repository directory.

Run the script:

python Analyzing Text Data with Word Clouds and N-grams.py
