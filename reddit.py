import praw
import json
import datetime
import os
from auth import client_id, client_secret, user_agent
from config import subreddit, limit

# Create a Reddit instance with your credentials
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Fetch hot posts
# hot_posts = reddit.subreddit(subreddit).hot(limit=limit)

# 500 posts with the flair "Seeking Support"
# HACK
hot_posts = reddit.subreddit(subreddit).search('flair:"Seeking Support"', limit=limit)

# Prepare the data
data = []
for i, post in enumerate(hot_posts):
    data.append({
        'id': i,
        'title': post.title,
        'content': post.selftext
    })

# Save the data to a file named after the subreddit and the current timestamp
now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%d_%H-%M')
filename = os.path.join('data', 'questions', f'{subreddit}_{timestamp}.json')
with open(filename, 'w') as f:
    json.dump(data, f)