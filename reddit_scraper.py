from dotenv import load_dotenv
import os
import praw
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    check_for_async=False
)
subreddit = reddit.subreddit("technology")

for post in subreddit.hot(limit=5):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}\n")