from tweepy import Stream
from tweepy import OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import time
import io
import pprint

consumer_key = []    

consumer_secret = []

access_token = []

access_token_secret = []

start_time = time.time()
keyword_list = ['North Korea']
order = 3
auth = OAuthHandler(consumer_key[order], consumer_secret[order])
auth.set_access_token(access_token[order], access_token_secret[order])

class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):
		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):
		#saveFile = io.open('raw_tweets.json','a',encoding='utf-8')

		while (time.time() - self.time) < self.limit:
			try:
				self.tweet_data.append(data)
				pprint.pprint (data)
				return True
			except BaseException as e:
				print ("failed ondata,", str(e))
				time.sleep(5)
				pass

		saveFile = io.open('raw_tweets.txt', 'w', encoding = 'utf-8')
		saveFile.write(u'[\n')
		saveFile.write(str(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()

	def on_error(self, status):
		print (status)


twitterStream = Stream(auth, listener(start_time, time_limit=60), domain='userstream.twitter.com')
#twitterStream.filter(track=keyword_list, languages=['en'])
#user = api.get_user("QiaozhiWang")
twitterStream.userstream(_with='followings',async=True)
 
"""class ReplyToTweet(StreamListener):
 
    def on_data(self, data):
    	print(data)
    	jsonData = json.loads(data.strip())
     
    	retweeted = tweet.get('retweeted', False)
    	from_self = tweet.get('user',{}).get('id_str','') == account_user_id
 
    	if retweeted is not None and not retweeted and not from_self:
 
	        tweetId = jsonData.get('id_str')
	        screenName = jsonData.get('user').get('screen_name')
	        tweetText = jsonData.get('text')
	        print(tweetText)
 
    def on_error(self, status):
        print(status)
 
if __name__ == '__main__':
    streamListener = ReplyToTweet()
    twitterStream = Stream(auth, streamListener)"""
