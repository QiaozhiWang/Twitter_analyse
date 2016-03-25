#=======================3/24/2016   Author: Qiaozhi=====================#
#-------------------use tagme to extract the tag in tweet---------------#
#--------------------tagme link: http://tagme.di.unipi.it---------------#
#--------------------------api_key: abc2051QQQ--------------------------#
#=======================================================================#

try:			#Run under python3
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
import requests
import pprint
import os, re
import pickle

#-------------------------put statuses into tagme--------------#
def tagme(text):
	url = 'http://tagme.di.unipi.it/tag?key=abc2051QQQ&text='+text+'&tweet=true'
	#url = 'http://maps.googleapis.com/maps/api/geocode/json?address=chicago&sensor=false'

	#json_obj = urllib2.urlopen(url).read().decode('utf-8')
	json_obj = urllib2.request.urlopen(url)

	data = json.loads(json_obj)
	pprint.pprint(data['annotations'])
	for term in data['annotations']:
		print("spot: %s, rho: %s"%(term['spot'],term['rho']))

#------------------------prepare statuses----------------------#
def preprocess(path,):
	f = open(path,'rb')	
	while True:
		try:
			statuses_list=pickle.load(f)
			for status in statuses_list:
				text = status.text
				print(text)
				text = re.sub(r'RT\s@\w+:\s|@\w+\s|#|http://.*$|http://.*\s', "", text)
				print(text)
				p_statuses.append(text)	
		except EOFError:
			break
	return p_statuses

if __name__ == '__main__':
	in_path = 'Kaite/Data'
	filenames = os.listdir()
	p_statuses=[]
	f_path = in_path +'/33042871/statuses_list.pickle' 	#33042871,4867410281
	p_statuses = preprocess(f_path)

	for text in p_statuses:
		if text is not null:
			tagme(text)

