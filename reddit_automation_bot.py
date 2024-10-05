import praw
import time
import csv
import os


# setting up Reddit API connection
reddit = praw.reddit(
    client_id='R6tP7GiTPo9VYvOCHhWzBA',
    client_secret='uoh0BvIoIET9KO_DqQG0cyrIRKl8tg',
    user_agent='pythonAutomation  by /u/kaustubhraii',
    username='kaustubhraii',
    password='rAIPARIVAR1',
)


# defining minecraft-related subreddits
minecraft_subreddits = ['Minecraft', 'MinecraftBuilds', 'MinecraftMemes']

# Defining keywords for upvoting, downvoting, and repling to comments
upvote_keywords = ['tutorial', 'build', 'guide', 'helpful']
downvote_keywords = ['spam', 'buy', 'promotion', 'sale']
commment_reply_keywords = ['help', 'question', 'build', 'tutorial']

# CSV file for data collection
csv_file = 'minecraft_data.csv'

# function to collect post data and store it in a CSV file
def collect_data(submission):
    # Check if the CSV file exists, if not, create it and add headers
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Post Title', 'Subreddit', 'Score', 'Upvote Ratio', 'URL'])

    # append post data to the CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([submission.title, submission.subreddit, submission.score, submission.upvote_ratio, submission.url])

