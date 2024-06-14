import tweepy
import random
import time

API_KEY                 = 'fuck0'
API_KEY_SECRET          = 'fuck2'

ACCESS_TOKEN            = 'fuck3'
ACCESS_TOKEN_SECRET     = 'fuck4'
BEARER_TOKEN            = 'fuck5'
CLIENT_SECRET           = 'fuck6'


def create_tweepy_bot():
    return tweepy.Client(consumer_key=API_KEY,
                         consumer_secret=API_KEY_SECRET,
                         access_token=ACCESS_TOKEN,
                         access_token_secret=ACCESS_TOKEN_SECRET,
                         bearer_token=BEARER_TOKEN)

tclient = create_tweepy_bot()

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)
tclientv1 = tweepy.API(auth)

def job(iterations):

    images = f'photos/{random.randint(0, 34)+1}.jpeg'
    media = tclientv1.media_upload(filename=images)
    media_id = media.media_id

    message = {'tweet': 'any tweet here who gives a shit'}
    try:
        tweet  = message['tweet']

        if len(tweet) <= 260:
            tclient.create_tweet(text=f'{tweet} #{iterations}', media_ids=[media_id])
            return 'success'
    except Exception as e:
        print(e)

    return 'failure'

i = 0
while True:
    job(i)
    i += 1
    time.sleep(15 * 60)
