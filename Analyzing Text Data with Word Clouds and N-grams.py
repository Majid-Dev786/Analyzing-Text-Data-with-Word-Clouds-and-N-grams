# Import necessary libraries and modules
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from nltk.util import ngrams

# Download required NLTK resources
nltk.download('punkt')

# Set parameters
n_gram_size = 3  # The size of n-grams to extract
top_n_grams = 10  # Number of top n-grams to display

# Read input text file
with open("words.txt", "r") as file:
    text = file.read().lower()

# Tokenize text and remove punctuation
tokenizer = nltk.RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(text)

# Generate Word Cloud
word_cloud = WordCloud(width=800, height=800, 
                       background_color='white', min_font_size=10).generate(' '.join(words))
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(word_cloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.title("Word Cloud")
plt.show()

# Generate n-grams
n_grams = list(ngrams(words, n_gram_size))

# Count n-grams
n_gram_counts = Counter(n_grams)

# Display top n-grams
top_n_grams = n_gram_counts.most_common(top_n_grams)
for n_gram, count in top_n_grams:
    print(f"{' '.join(n_gram)}: {count}")