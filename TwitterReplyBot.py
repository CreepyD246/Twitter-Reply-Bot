import tweepy
import time

def get_info(credential):
    cred_dict = {}
    with open("C:\\Users\\denis\\Desktop\\New Videos\\Tweepy Tutorials\\Tweepy Reply Bot Tutorial [Python]\\BOT\\bot_info.txt", "r") as f:
        for line in f.read().split("\n"):
            cred_dict[line.split("=")[0]] = line.split("=")[1]
    return cred_dict[credential]

# Credentials and Token Info
api_key = get_info("api_key")
api_secret_key = get_info("api_secret_key")
access_token = get_info("access_token")
secret_access_token = get_info("secret_access_token")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)

#ACTUAL TUTORIAL CODE
bot_id = int(api.me().id_str)
mention_id = 1

words = ["why", "how", "when", "what", "?"]
message = "If you have any questions, feel free to send us a DM @{}"

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Mention tweet found")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if [word in mention.text.lower() for word in words]:
                try:
                    print("Attempting to reply...")
                    api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                    print("Successfully replied :)")
                except Exception as exc:
                    print(exc)
    time.sleep(15)