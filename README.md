first-machine-learning-youtube-comment-fetching
          This Python project fetches comments from a YouTube video using the YouTube Data API, processes the comments with NLP techniques, and performs sentiment analysis.

Features
      Fetch up to 200 comments from any public YouTube video.

      Text preprocessing including tokenization, stopword removal, and stemming using NLTK.

      Word frequency analysis.

      Sentiment analysis of comments using TextBlob.

     Displays raw comments, word frequency, and sentiment summary.
Requirements
    Python 3.6+

    Google API Client Library

   NLTK

   TextBlob
Code Overview
  get_video_comments(video_id, api_key, max_comments=200): Fetches comments from the specified YouTube video.

  process_comments(comments): Tokenizes, removes stopwords, and stems words from the comments.

  get_word_frequencies(words): Counts the frequency of words.

  analyze_sentiments(comments): Performs sentiment analysis, categorizing comments as positive, neutral, or negative.

  main(): Coordinates fetching, processing, and displaying results.
License
  This project is licensed under the MIT License.



