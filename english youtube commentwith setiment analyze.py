import googleapiclient.discovery
import googleapiclient.errors
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from textblob import TextBlob

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def get_video_comments(video_id, api_key, max_comments=200):
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Fetch comments
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            if len(comments) >= max_comments:
                break

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break  # No more pages of comments

    return comments

def process_comments(comments):
    # Set up NLTK tools
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # Tokenize, remove stopwords, and stem the words
    filtered_words = []
    for comment in comments:
        words = word_tokenize(comment.lower())  # Tokenize and convert to lowercase
        filtered_words += [stemmer.stem(word) for word in words if word.isalnum() and word not in stop_words]

    return filtered_words

def get_word_frequencies(words):
    # Get word frequencies
    word_freq = Counter(words)
    return word_freq
def analyze_sentiments(comments):
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}

    for comment in comments:
        blob = TextBlob(comment)
        polarity = blob.sentiment.polarity  # -1 = very negative, +1 = very positive

        if polarity > 0.1:
            sentiments["positive"] += 1
        elif polarity < -0.1:
            sentiments["negative"] += 1
        else:
            sentiments["neutral"] += 1

    return sentiments


def main():
    # YouTube video ID and API Key
    video_id = "4G2EO6bqaRo"  # Replace with the desired video ID
    api_key = ""  # enter your API key

    # Fetch the comments
    print("Fetching comments...")
    comments = get_video_comments(video_id, api_key)

    print(f"Fetched {len(comments)} comments.")
    print("\nAll Raw Comments:")
    for i, comment in enumerate(comments, 1):
        print(f"{i}. {comment}")


    # Process the comments
    print("Processing comments...")
    filtered_words = process_comments(comments)

    # Get word frequencies
    word_freq = get_word_frequencies(filtered_words)# Analyze sentiment
    print("\nAnalyzing sentiment...")
    sentiment_results = analyze_sentiments(comments)
    print("\nSentiment Summary:")
    for sentiment, count in sentiment_results.items():
        print(f"{sentiment.capitalize()}: {count}")



    # Display word frequency results
    print("Word Frequency (Top 40):")
    for word, freq in word_freq.most_common(40):
        print(f"{word}: {freq}")

    # Unique words count
    print(f"\nUnique words count: {len(set(filtered_words))}")

if __name__ == "__main__":
    main()
