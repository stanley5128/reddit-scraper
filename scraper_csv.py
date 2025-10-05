import praw
import csv

reddit = praw.Reddit(
    client_id="vFz4Y9uwn6nAWlfwyfsO6w",
    client_secret="QV3URyR1FhOyjry7OYrxacXiuQ4rRg",
    user_agent="reddit_scraper_app by u/Due-Cod-7341"
)

subreddit = reddit.subreddit("technology")

with open("reddit_posts.csv", "w", 
          newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Score", "URL"])

    for post in subreddit.hot(limit=10):
        writer.writerow([post.title, post.score, post.url])
        print(f"Saved: {post.title}")