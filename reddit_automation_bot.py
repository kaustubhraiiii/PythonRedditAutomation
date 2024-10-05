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

# function to scan posts and upvote/downvote based on keywords
def check_and_vote_on_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.new(limit=10):
        print(f"Checking post: {post.title}")

        # collect data for analysis
        collect_data(post)

        # convert the post title to lowercase for case-insensitive matching
        title_lower = post.title.lower()

        # check for upvote keywords
        if any(keyword in title_lower for keyword in upvote_keywords):
            post.upvote()
            print(f"Upvoted post: {post.title}")

        # check for downvote keywords
        elif any(keyword in title_lower for keyword in downvote_keywords):
            post.downvote()
            print(f"Downvoted post: {post.title}")
        
        time.sleep(5) # Pause to respect Reddit's rate limits

# Function to scan comments and reply based on keywords
def check_and_reply_to_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    for comment in subreddit.comments(limit=10):
        print(f"Checking comment: {comment.body}")

        # convert the comment body to lowercase for case-insensitive matching
        comment_lower = comment.body.lower()

        # check for keywords to reply
        if any(keyword in comment_lower for keyword in comment_reply_keywords):
            reply_text = "Hey! It looks like you need help with something related to Minecraft. You can check out [Minecraft Wiki](https://minecraft.fandom.com/wiki/Minecraft_Wiki) for more information!"
            comment.reply(reply_text)
            print(f"Replied to comment: {comment.body}")

        time.sleep(5) # pause to respect reddit's rate limits

