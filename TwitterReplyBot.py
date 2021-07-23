#Importing modules/libraries
import tweepy
import time

# Initialization code
auth = tweepy.OAuthHandler("YOUR API KEY", "YOUR API SECRET KEY")
auth.set_access_token("YOUR ACCESS TOKEN", "YOUR SECRET ACCESS TOKEN")
api = tweepy.API(auth)

# Some important variables which will be used later
bot_id = int(api.me().id_str)
mention_id = 1
words = ["why", "how", "when", "what", "?"]
message = "If you have any questions, feel free to send us a DM @{}"

# The actual bot
while True:
    mentions = api.mentions_timeline(since_id=mention_id) # Finding mention tweets
    # Iterating through each mention tweet
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        # Checking if the mention tweet is not a reply, we are not the author, and
        # that the mention tweet contains one of the words in our 'words' list
        # so that we can determine if the tweet might be a question.
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc)
    time.sleep(15) # The bot will only check for mentions every 15 seconds, unless you tweak this value
