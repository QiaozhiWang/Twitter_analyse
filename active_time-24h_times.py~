import os
import pickle
import datetime
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab
time_now = datetime.datetime.now()

def sep_rtp(user_id):
	all_time = []		#time for all activation
	ot_time = []		#time for original tweet
	rted_time = []		#time for a tweet be retweeted 
	rt_orig_time = []	#the original time of retweeted tweet
	rp_time = []		#time for reply
	rt_delay = []		# rted_time - rt_orig_time
	f2 = open("Data/%s/profile.pickle"%user_id,'rb')
	profile = pickle.load(f2)
	f_path = "Data/%s/statuses_list.pickle"%user_id
	if not os.path.exists(f_path):
		print("Can't find user %s's statuses_list. Probably user doesn't have any tweet!"%user_id)
		pass
	else:
		f = open("Data/%s/statuses_list.pickle"%user_id,'rb')
		while True:									#Since pickle can't read to the end automatically.
			try:		
				statuses=pickle.load(f)
				for tweet in statuses:
					status_time = tweet.created_at
					hour = (24+status_time.hour-6)%24	#change to central american time
					x_time = hour+status_time.minute/60
					all_time.append(x_time)
					if tweet.text[0:4] == 'RT @':	#retweet
						rted_time.append(x_time)						
						try:							#try to get original tweet time
							original_time = tweet._json['retweeted_status']['created_at']
							p = original_time.find('+')
							time = original_time[4:p-1]+original_time[p+5:]
							date = datetime.datetime.strptime(time, '%b %d %H:%M:%S %Y')
							hour_orig = (24+date.hour-6)%24
							orig_time = date.hour+date.minute/60
							rt_orig_time.append(orig_time)
							rt_delay.append((status_time.month-date.month)*30+abs(status_time.day-date.day)+abs(x_time-orig_time)/24)
						except KeyError as ek:
							print(str(ek)+", Can't find original retweet time! User: %s"%user_id)
							continue
					elif tweet.text[0] == '@':		#reply
						rp_time.append(x_time)
					else:
						ot_time.append(x_time)		#original tweet
			except EOFError:						#Pickle reads to the end of the file 	
				break
	return profile, all_time, ot_time, rted_time, rt_orig_time, rp_time, rt_delay

filename = os.listdir("Data")
#select = np.random.choice(len(filename),40)		#select parts of file to show
#for i in range(0,40):
for i in range(0,len(filename)):
	user_id = filename[i]	
	(profile, all_time, ot_time, rted_time, rt_orig_time, rp_time, rt_delay) = sep_rtp(user_id)
	if len(all_time) >= 500:
		fig = plt.figure()
		num_bins = 50
		if len(all_time) != 0:
			ax = fig.add_subplot(4,1,1)
			ax.set_xlim([0,24])		
			n, bins, patches = ax.hist(all_time, 100, facecolor='green', alpha=0.5)
			plt.title("User: %s, total_tweets: %s, time_zone: %s"%(profile['screen_name'],len(all_time),profile['time_zone']))

		if len(rt_delay) != 0:
			ax = fig.add_subplot(4,1,4)
			n, bins, patches = ax.hist(rt_delay, 100, facecolor='green', alpha=0.5)
			plt.title("Time delay.")

		if len(ot_time) != 0:
			ax1 = fig.add_subplot(4,2,3)
			ax1.set_xlim([0,24])
			n, bins, patches = ax1.hist(ot_time, num_bins, facecolor='green', alpha=0.5)
			plt.title("Personal tweet time, #: %s"%(len(ot_time)))

		if len(rp_time) != 0:
			ax2 = fig.add_subplot(4,2,5)
			ax2.set_xlim([0,24])
			n, bins, patches = ax2.hist(rp_time, num_bins, facecolor='green', alpha=0.5)
			plt.title("Rp time, #: %s"%(len(rp_time)))

		if len(rted_time) != 0:
			ax3 = fig.add_subplot(4,2,4)
			ax3.set_xlim([0,24])
			n, bins, patches = ax3.hist(rted_time, num_bins, facecolor='green', alpha=0.5)
			plt.title("Rt time, #: %s"%(len(rted_time)))

		if len(rt_orig_time) != 0:
			ax4 = fig.add_subplot(4,2,6)
			ax4.set_xlim([0,24])
			n, bins, patches = ax4.hist(rt_orig_time, num_bins, facecolor='green', alpha=0.5)
			plt.title("Original time of rt, #: %s"%(len(rt_orig_time)))

		#mng = plt.get_current_fig_manager()			#show full screen
		#mng.full_screen_toggle()
		fig.tight_layout()
		plt.show()
	else:
		continue

