import json
import time
import requests
import re

import tweepy
import threading

tclient = tweepy.Client(consumer_key            =   "9XZsu6Bc5Jhfz0c4k7VOEjV9B",
                        consumer_secret         =   "0QoGLhFNyC1ObeQy0tdvye0FpfiZoQGaJA7jqssj76fmAjR6H3",
                        access_token            =   "1557438727810699268-DBqQu5bQGZtQGjKRilocYPr0pjR795",
                        access_token_secret     =   "4lW1EmiXaQJGBFpwEe1d5qcR4hp3lVYZt2ujlVrkLLzCA",
                        bearer_token            =   "AAAAAAAAAAAAAAAAAAAAAKBntwEAAAAAYNHLPHdwPZqu42XVaRbOgasQs34%3DUQu079DmEqZfa600Sb6MuFzgxT1bte8kG4tHy9Sr8FfJoToBFg")

auth = tweepy.OAuth1UserHandler("9XZsu6Bc5Jhfz0c4k7VOEjV9B", "0QoGLhFNyC1ObeQy0tdvye0FpfiZoQGaJA7jqssj76fmAjR6H3")
auth.set_access_token(
    "1557438727810699268-DBqQu5bQGZtQGjKRilocYPr0pjR795",
    "4lW1EmiXaQJGBFpwEe1d5qcR4hp3lVYZt2ujlVrkLLzCA"
)
auth_client = tweepy.API(auth)

url = 'https://deepstatemap.live/api/history/'
content = json.loads(requests.get(url=url).content.decode('utf-8'))
latest = content[0]
l_keys = latest.keys()

cache = [None]

iterations = 0
def job():
    while True:
        tweet = f'I will post this every hour until the election #{iterations} https://tenor.com/view/jpr-gif-22001827'
        tclient.create_tweet(text=tweet)
        iterations+=1
        time.sleep(3600)

t = threading.Thread(target=job)
t.start()


while True:
    time.sleep(1)

    try:
        descriptionUA_raw = latest['description']
        descriptionUA = re.sub(re.compile('<.*?>'), '', descriptionUA_raw)

        descriptionEN_raw = latest['descriptionEn']
        descriptionEN = re.sub(re.compile('<.*?>'), '', descriptionEN_raw)

        desc = f"{descriptionUA}\n {descriptionEN}\nupdated: {latest['updatedAt'].split('T')[0]}\ncreated: {latest['createdAt'].split('T')[0]}\nData from: deepstatemap.live"

        if cache[-1] != desc:
            cache.append(desc)

            desc_en = f"{descriptionEN}\nupdated: {latest['updatedAt'].split('T')[0]}\ncreated: {latest['createdAt'].split('T')[0]}\nData from: deepstatemap.live"
            desc_ua = f"{descriptionUA}\nдата оновлення: {latest['updatedAt'].split('T')[0]}\nдата створення: {latest['createdAt'].split('T')[0]}\nПдані з: deepstatemap.live"

            tclient.create_tweet(text=desc_en)
            tclient.create_tweet(text=desc_ua)

    except Exception as e:
        print(e)
    
#tclient.create_tweet(text='fuck')
