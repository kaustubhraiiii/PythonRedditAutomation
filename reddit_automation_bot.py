import praw
import time
import csv
import os

# Set up Reddit API connection
reddit = praw.Reddit(
    client_id='yuMWMqX71zFBwU7kLt2wXQ',
    client_secret='_WoRE5vvH5WGSopcmYzUczsB9oZVog',
    user_agent='minecraftAutomation by /u/kaustubhraii',
    username='kaustubhraii',
    password='rAIPARIVAR1'
)

# Define Minecraft-related subreddits
minecraft_subreddits = ['Minecraft', 'Minecraftbuilds', 'MinecraftMemes']

# Define keywords for upvoting, downvoting, and commenting
upvote_keywords = ['tutorial', 'build', 'guide', 'helpful']
downvote_keywords = ['spam', 'buy', 'promotion', 'sale']
comment_reply_keywords = ['help', 'question', 'build', 'tutorial']

# CSV file for data collection
csv_file = 'minecraft_data.csv'

# Function to collect data and store it in a CSV file
def collect_data(submission):
    if not os.path.exists(csv_file):
        # If CSV file does not exist, create it and add headers
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Post Title', 'Subreddit', 'Score', 'Upvote Ratio', 'URL'])
    
    # Append post data to the CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([submission.title, submission.subreddit, submission.score, submission.upvote_ratio, submission.url])

# Function to scan posts and upvote/downvote based on keywords
def check_and_vote_on_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    for post in subreddit.new(limit=10):  # Check the 10 most recent posts
        print(f"Checking post: {post.title}")
        
        # Collect data for analysis
        collect_data(post)

        # Convert the post title to lowercase for case-insensitive matching
        title_lower = post.title.lower()

        # Check for upvote keywords
        if any(keyword in title_lower for keyword in upvote_keywords):
            post.upvote()
            print(f"Upvoted post: {post.title}")
        
        # Check for downvote keywords
        elif any(keyword in title_lower for keyword in downvote_keywords):
            post.downvote()
            print(f"Downvoted post: {post.title}")
        
        time.sleep(5)  # Pause to respect Reddit's rate limits

# Function to scan comments and reply based on keywords
def check_and_reply_to_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    
    for comment in subreddit.comments(limit=10):  # Check the 10 most recent comments
        print(f"Checking comment: {comment.body}")
        
        # Convert the comment body to lowercase for case-insensitive matching
        comment_lower = comment.body.lower()

        # Check for keywords to reply
        if any(keyword in comment_lower for keyword in comment_reply_keywords):
            reply_text = "Hey! It looks like you need help with something related to Minecraft. You can check out [Minecraft Wiki](https://minecraft.fandom.com/wiki/Minecraft_Wiki) for more information!"
            comment.reply(reply_text)
            print(f"Replied to comment: {comment.body}")
        
        time.sleep(5)  # Pause to respect Reddit's rate limits

# Main function to run the bot
def run_bot():
    while True:
        try:
            # Scan through each Minecraft-related subreddit
            for subreddit_name in minecraft_subreddits:
                print(f"Scanning subreddit: {subreddit_name}")
                
                # Check and vote on posts
                check_and_vote_on_posts(subreddit_name)
                
                # Check and reply to comments
                check_and_reply_to_comments(subreddit_name)
                
                time.sleep(60)  # Wait 1 minute before scanning again

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Wait 1 minute before retrying

# Run the bot
run_bot()
