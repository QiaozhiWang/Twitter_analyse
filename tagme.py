#=======================3/24/2016   Author: Qiaozhi=====================#
#-------------------use tagme to extract the tag in tweet---------------#
#--------------------tagme link: http://tagme.di.unipi.it---------------#
#--------------------------api_key: abc2051QQQ--------------------------#
#=======================================================================#
import json
import pprint
import os, re
import pickle
import time
import urllib
from nltk.tokenize import sent_tokenize, word_tokenize
import unicodedata
import socket

try:
    # UCS-4
    highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
except re.error:
    # UCS-2
    highpoints = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')
# mytext = u'<some string containing 4-byte chars>'

#-------------------------put statuses into tagme--------------#
def tagme(tag_text):
	text = tag_text
	url = 'http://tagme.di.unipi.it/tag?key=abc2051QQQ&text='+text+'&tweet=true&include_categories=true'
	#url = 'http://maps.googleapis.com/maps/api/geocode/json?address=chicago&sensor=false'
	text_dic = {}
	try:
		json_obj = urllib.request.urlopen(url,timeout=1).read().decode('utf-8')
		data = json.loads(json_obj)
		if data['annotations']:
			tag_list = data['annotations']
			#print(tag_list)
			for tag in tag_list:
				try:
					text_dic[tag['title']] = [tag['spot'],tag['rho']]
				except:
					continue
	except urllib.error.HTTPError as e:
		print(e)
		text_dic = tagme(text)
	except urllib.error.URLError as e:
		print(e)
		text_dic = tagme(text)
	except socket.timeout as e:
		print(e)
		text_dic = tagme(text)
	return text_dic

#------------------------prepare statuses----------------------#
def preprocess(path,):
	text = []
	f = open(path,'rb')	
	while True:
		try:
			statuses_list=pickle.load(f)
			for status in statuses_list:
				tweet = status.text
				#print(tweet)
				sents = sent_tokenize(tweet)
				text = ""
				for sent in sents:
					#print("sent: ", sent)
					sent_text = re.sub(r'RT\s@\w+:\s|@\w+\s|#|http://.*$|http://.*\s|https://.*$|https://.*\s|\n|\\U\w+', "", sent)
					sent_text = highpoints.sub("", sent_text)
					tokens = word_tokenize(sent_text)
					words = [w.lower() for w in tokens if w.isalpha() or w.isalnum()]
					sent_text = '+'.join(words)
					text = text+'+'+sent_text
					#print(text)
				p_statuses.append(text)	

		except EOFError:
			break
	return p_statuses

if __name__ == '__main__':
	all_tag = []
	in_path = 'Kaite/Data'
	filenames = os.listdir(in_path)
	p_statuses=[]
	f_path = in_path +'/33042871/statuses_list.pickle' 	#33042871,4867410281
	p_statuses = preprocess(f_path)
	#pprint.pprint(p_statuses)
	for text in p_statuses:	
		try:
			if not text:
				all_tag.append({})
			print(text)
			text_dic = tagme(text)
			pprint.pprint(text_dic)
		except UnicodeEncodeError:
			#print("Contain some non-English words!")
			text = unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode('utf-8')
			text_dic = tagme(text)
			pprint.pprint(text_dic)
			continue
		all_tag.append(text_dic)
	pickle.dump(all_tag,open('Kaite/Data/33042871/all_tags.pickle','wb'))

		#pprint.pprint(tags)



