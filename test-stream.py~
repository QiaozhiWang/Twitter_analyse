from tweepy import Stream
from tweepy import OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import time
import io
import pprint

consumer_key = ["2hdYcnutFkKRUqb64ayNRpVgB", 
                "kyIWa92Lv2u1Ft9a0i8LUpc0I",
                "EoTeL21ovvTpk81ULCyo2yOuK",
                "4R9U5d6KsTSXq1tP6pQtdiwXF",
                "bbfeNT16k4DjQ2vSv62ewc1Rq",
                "r92gGp2OgUSdub2zxVxqNwg5C",
                "0QISn6rtQT4Q2ifL5XBh7A",
                "zD3EF2QNb5K8mPQUJ9IlhRZZP",
                "noZMwDRWdpuwpr29BM0GcswNM",        #bjtu-mail
                "FerszN3dUw1121tSoAqkSxypr",
                "wV1DkaBOOLWpaoft6R7iaIpKW"]    

consumer_secret = ["g1IiDYdk397gu1nMwSwIM1YzwANormW0HITpkE1QZECoJyVqSU", 
                    "Gk3Ir3wT2BqD3PAnYAIWpx3NBAcVPJ6tseLAx6JwgfhPS7QrV2",   #cannot be authenticated
                    "1QpFmh01XJ2zTpSCZBcukb29nyLWORYwVfPFzZbLFYcv5Ove9M",
                    "M5Z4IKQJfAOjToKx6wPFJ6XUQxMNoI3BgZwNI070FAGZHyTqtV",
                    "b0ZA9cjg5YWtPwtqbofmxOioaWUbOZtxbfAleq5kwLdwESpYxf",
                    "xLlIUCE1hxw7AdYw97AeOvgPyeqKAnsdtQB18mRYIyw68abYd9",   # invalid or expired token
                    "sC8AedqrqzJmdgAl2q03gwAzkJteS7EyI6gDXBpB0k",
                    "FLlfj1z1Fs6C3zv1E3HR6u4aj27Oz5xCSdroUKQT7MTErUoyMo",
                    "SzpujWtwUpKPv3pzMui0pXS1Z3qweg6HDiNM9jzTExDqVMeM4J",
                    "lNnSUgCwTaYUCZDBPv3sBVREHdPfryPnpeDNmTq9Br8rWRITfK",
                    "P82YYQ0d2UQponRoOpKC2tkTArnPN4MqfqOWAsZSxUeO4kPvox"]

access_token = ["3476728637-voVX1ieFUiWRgbHpriUjP2gQghrwZ4tIQfMwQDA", 
                "4324960994-7PrrNre8WnIMYsUXOkydRZW3qlpp3HWA6Z3CtZq",
                "4324993344-ysmV05aHDQXaTMAf6EUF8LPHAUWukNIzeXc1b59",
                "3476728637-OefRDE2cwofR09zASUdMQnT18jXRm8z7P1ZcbtQ",
                "4324960994-0AQBTcHufighXVA07jAAdXwbnbiZoDkowed2z9g",
                "4324993344-m8gMzbZwQUsN3FfKZDHtTZdfWt3vsBpscv6izj9",
                "831613928-nF2CfdZRIG1NaVcvvtlCUMNKMuYtrSG2QNyZgZQs",
                "3314186540-taoZfKzfR1msaRJZMOXLU9lAzoL8gUIBDdq1Khk",
                "4324939938-TwZl1AcFSlO7arbkCAy5AbtmELlD2rKsWJnTolV",
                "4794002696-N8d5GMZksZnYFynG9exjr0ziJ0x5EX09Kiv2a5E",
                "4324960994-7PrrNre8WnIMYsUXOkydRZW3qlpp3HWA6Z3CtZq"]

access_token_secret = ["6NhftECqHKhschl1iPTecmxU57VyHBoqqaaqWKulvsIAG", 
                        "pfEjvxbXQTjjbZKFuPiuDu2La7w38jiouDZhkTzaGxnr3",
                        "oWgflkDZzB3paUyESfHkJbacNrNwYFkEtbrkzKNqvffQ9",
                        "vCngeSyxCTXm9bwv17yo7IQB7l6I6FRhbrC5KUUouZ5hv",
                        "YiCmlepNodWQ9oLSHeZ93p8J20Vo7bh9pK64A79lmUaRh",
                        "7FQFB08DysexjmzIDp8HODukOEztd55glzvsB8GVZPBPV",
                        "ll3Gt5WXTHmoqw5AR0das9V2NlwLvmzsO4BPeNBXU",
                        "ZaHC5mgZhTNkp3bvY9alFc1q7zzfYPn9tbiRhfQ5eHed4",
                        "l7ImKhWvZSxKQHUFi93pL4STPGvpgsyQqpUYaiIovXkZb",
                        "o2BLrjaTsFrJ3YvvvqqYWNNTAtpxEA0DgHDD19vcSETTg",
                        "pfEjvxbXQTjjbZKFuPiuDu2La7w38jiouDZhkTzaGxnr3"]

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