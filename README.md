# Sentiment Analysis System
Build a sentence-level sentiment analysis model using traditional machine learning approaches and compare the performances of these models on standard classification metrics

## Data collection
To collect positive reviews, I will scrape reviews from the top 100 movies sorted by popularity in the following link: https://www.imdb.com/search/title/?groups=top_100. Conversely, I will collect negative reviews from the top 100 movies with the lowest rating in this link: https://www.imdb.com/chart/bottom.

The collection process will follow these steps:

1. Get links of movies: I will obtain 30 movie links from each of the two links mentioned above.
2. Get links of movie reviews: For each movie link obtained in step 1, I will extract the link to its reviews by finding the **User reviews** and getting its `href`.
3. Collect reviews for each link of movie reviews: For each movie, I will collect about 400 reviews. For each block of review, I will get user name, title, content, rating and date of review.
4. Export two files containing the collected data.


## Data labeling

I performed preprocessing and labeling on the collected data from IMDb in the following order:

1. Tokenization: I separated each review into sentences and considered each sentence as a separate review. The entire dataset was created by splitting all the sentences in the raw dataset.
2. Remove special symbols: I removed special symbols from each sentence to clean the text data and ensure consistency.
3. POS Tagging: POS tagging was conducted to identify the part-of-speech of each word in the sentences. This information was needed for lemmatization.
4. Lemmatization: I performed lemmatization on each POS-tagged sentence to reduce words to their base or dictionary form, which helps in grouping similar words together.
5. Sentiment Rule-Based Tagging: Following tutorials and research, I used the `sentiwordnet` submodule of the `nltk` library for the labeling process. `sentiwordnet` provides polarity scores for individual words, not entire sentences. I used these scores to compute the polarity of each lemmatized sentence.

The core idea behind the labeling process is to count and summarize the polarity scores of each word in the lemmatized sentences (after preprocessing). The resulting label can be one of four cases: `positive`, `negative`, `neutral`, or `None`, depending on the overall polarity score of the sentence.

## Benchmarking
I choose 2 techniques to extract features: **TF-IDF** and **DOC2VEC**, and 3 traditional machine learning models to train and evaluate: **Random Forest Classifier (RFC)**, **Gradient Boosting Classifier (XGB)** and **Logistic Regression (LR)**.

Comment on evaluation:
- The accuracy of **TF-IDF** is about 15 to 20% higher than **doc2vec**.
- With **TF-IDF**, **LR** has the highest accuracy (0.89875), and **XGB** has the lowest result (0.7380625)
- With **doc2vec**, 3 models give results with no obvious difference

