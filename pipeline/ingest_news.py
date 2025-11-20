from newspaper import Article
import feedparser

RSS_FEEDS = [
     #"https://realty.economictimes.indiatimes.com/rss/topstories",
    #"https://jainoncor.com/blog/feed"         # Add more RSS URLs
    #"https://www.hindustantimes.com/feeds/rss/india-news/rssfeed.xml",
    #"https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml",
    #"https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml",
    "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://indianexpress.com/feed/"
]

def fetch_articles():
    articles = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:  # Limit to 5 per source for now
            url = entry.link
            try:
                article = Article(url)
                article.download()
                article.parse()
                articles.append({
                    "title": article.title,
                    "text": article.text,
                    "url": url,
                    "published": entry.published
                })
            except Exception as e:
                print(f"Error parsing article: {e}")
    return articles