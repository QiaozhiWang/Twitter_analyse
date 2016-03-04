import os
import pickle
import datetime
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab
import time

#=====================extract active time,t\rt\rp time====================#
def sep_rtp(user_id):
	all_time = []		#time for all activation
	pt_time = []		#time for user personal tweet
	rted_time = []		#time for a tweet be retweeted 
	rt_orig_time = []	#the original time of retweeted tweet
	rp_time = []		#time for reply
	rt_delay = []		# rted_time - rt_orig_time
	deff_time = []
	whole_time = []
	f2 = open("Data/%s/profile.pickle"%user_id,'rb')
	profile = pickle.load(f2)
	screen_name = profile["screen_name"]
	f_path = "Data/%s/statuses_list.pickle"%user_id
	# if user does not have any statuses, this file will not exist
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
					whole_time.append(status_time)
					hour = (24+status_time.hour-6)%24   #change to central american time
					t_24 = hour+status_time.minute/60
					all_time.append(t_24)
					if tweet.text[0:4] == 'RT @':   #retweet   
						rted_time.append(t_24)                   
						try:                            #try to get original tweet time
							original_time = tweet._json['retweeted_status']['created_at']
							p = original_time.find('+')
							o_time = original_time[4:p-1]+original_time[p+5:]
							orig_date = datetime.datetime.strptime(o_time, '%b %d %H:%M:%S %Y')
							hour_orig = (24+orig_date.hour-6)%24
							orig_24 = orig_date.hour+orig_date.minute/60
							rt_orig_time.append(orig_24)
							d1_ts = time.mktime(status_time.timetuple())
							d2_ts = time.mktime(orig_date.timetuple())
							rt_delay.append((d1_ts-d2_ts)/60/60/24)
							#print ("Retweet time: %s, Tweet original time: %s, difference: %s"%(status_time,orig_date,(d1_ts-d2_ts)/60))
	                        #print("Original time is: ", orig_time)
						except KeyError as ek:
							print(str(ek)+", Can't find original retweet time! User: %s"%user_id)
							continue
					elif tweet.text[0] == '@':		#time of reply
						rp_time.append(t_24)
					else:
						pt_time.append(t_24)		#time of user personal tweet
			except EOFError:						#Pickle reads to the end of the file 	
				break

		for i in range(1,len(whole_time)):
			d3_ts = time.mktime(whole_time[i].timetuple())
			d4_ts = time.mktime(whole_time[i-1].timetuple())
			deff_time.append((d4_ts - d3_ts)/60/60/24)		#convert to hours
		print ("Differen of time: \n%s"%deff_time)
	return profile,all_time,pt_time,rted_time,rt_orig_time,rp_time,rt_delay,deff_time,screen_name

#==========================================plot data=================================================#
def plot_hist(data_list,num_bins,position,x_range,y_range,fig,ax_title):
	if len(data_list) != 0:
		ax = fig.add_subplot(position)
		if x_range != [0,0]: 			# if x_range = [0, 0]
			ax.set_xlim(x_range)
		if y_range!=[0,0]:
			ax.set_ylim(y_range)
		n, bins, patches = ax.hist(data_list, num_bins, facecolor='green', alpha=0.5)
		bin_max = np.where(n==n.max())		# get the heighest point of the histrogram
		#nmax = bins[bin_max]				# get the position(hour) of n max
		nmax = n.max()
		less_active=sorted(range(len(n)),key=lambda k: n[k])		#key sequence
		#less_active = sorted(n)
		#print("less_active: %s"%less_active)
		#print([bins[less_active[0]],0], [bins[less_active[0]],nmax])
		ax.plot([bins[less_active[0]],bins[less_active[0]]],[0,nmax],'r--')		#[x1,x2],[y1,y2]
		plt.title(ax_title)
	return fig,nmax

def plot_xy(data_list,position,fig,title):
	ax = fig.add_subplot(position)
	x = np.arange(0,len(data_list),1)
	ax.set_xlim([0,len(data_list)])
	plt.scatter(x, data_list,s=2)
	#plt.plot(x, data_list,"b-")
	plt.title(title)
	return plt

#======================main() function==========================#
if __name__ == '__main__':
	filename = os.listdir("Data")
	select = np.random.choice(len(filename),10)		#select parts of file to show
	for i in range(0,10):
		user_id = filename[select[i]]
		(profile, all_time, pt_time, rted_time, rt_orig_time, rp_time, rt_delay, deff_time,screen_name) = sep_rtp(user_id)
		if len(all_time) >= 500:
			print("Should have pictures here!")
			num_bins = 50
			# usual active hour
			fig1 = plt.figure(1,figsize=(8,10)) 			
			(fig1,nmax) = plot_hist(all_time,num_bins,311,[0,24],[0,0],fig1,"Totle activities time%s  "%screen_name+"%s"%(len(all_time)))
			y_range = [0, nmax]
			(fig1,nmax) = plot_hist(pt_time,num_bins,323,[0,24],y_range,fig1,"%s's personal tweets time "%screen_name+"%s"%(len(pt_time)))
			(fig1,nmax) = plot_hist(rted_time,num_bins,324,[0,24],y_range,fig1,"%s's retweets time "%screen_name+"%s"%(len(rted_time)))
			#unactive_time = less_active[:10]
			(fig1,nmax) = plot_hist(rp_time,num_bins,325,[0,24],y_range,fig1,"%s's reply time "%screen_name+"%s"%(len(rp_time)))
			(fig1,nmax) = plot_hist(rt_orig_time,num_bins,326,[0,24],y_range,fig1,"%s's retweets original time "%screen_name+"%s"%(len(rt_orig_time)))
			fig1.tight_layout()
			fig2 = plt.figure(2,figsize=(8,10))
			plt = plot_xy(deff_time,311,fig2,"%s's difference of active time. Unit: day"%screen_name)
			plt = plot_xy(rt_delay,312,fig2,"%s's retweet delay. Unit: day"%screen_name)
			(fig2,nmax) = plot_hist(deff_time,num_bins,325,[0,0],[0,0],fig2,"hist of deff_time. Unit: day")
			(fig2,nmax) = plot_hist(rt_delay,num_bins,326,[0,0],[0,0],fig2,"hist of rt_delay. Unit: day")
			fig2.tight_layout()
			plt.show()			
