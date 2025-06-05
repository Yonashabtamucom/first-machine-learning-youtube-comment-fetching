YouTube Comment Analyzer

A Python-based NLP tool to extract, process, and analyze comments from YouTube videos using the YouTube Data API.

Quickly gain insights from user comments with sentiment analysis, word frequency statistics, and more.

---
 Description

Ever wondered what people are really saying about a YouTube video?

YouTube Comment Analyzer** helps you:

-  Fetch the latest comments from any video
-  Clean and analyze the text
-  Determine sentiment trends
-  Identify the most commonly used words

Whether you're a **content creator**, **data scientist**, or just **curious**, this tool gives you a deeper look into YouTube audience engagement.

---

Features

- Fetches up to **200 top-level comments**
- Removes stopwords and applies stemming
- Performs **sentiment analysis** (Positive, Neutral, Negative)
- Displays the **top 40 most frequent words**
- Built with **NLTK**, **TextBlob**, and the **YouTube Data API v3**

---

Requirements

Install dependencies:

pip install google-api-python-client nltk textblob

Download NLTK resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')

Setup Instructions

Get a YouTube API Key:

Go to Google Cloud Console
Enable YouTube Data API v3
Create a new API key under APIs & Services > Credentials

Configure the script:
video_id = "YOUR_VIDEO_ID"
api_key = "YOUR_API_KEY"

Customization Tips

Modify max_comments in the get_video_comments() function to fetch more or fewer comments.
Add a CSV export function to save comments or results.
Adjust sentiment thresholds in analyze_sentiments() for more nuanced categories.

 License
 
This project is licensed under the MIT License — free to use and modify.

 Contributing

Pull requests and suggestions are welcome!
If you like this tool, give it a ⭐️ on GitHub!

Author
Made with ❤️ by Yonashabtamucom




