import datamaker
import time
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
import matplotlib as mpl
from statistics import mean
plt.style.use('seaborn-whitegrid')


max_reps = 100		# How many iterations-Measurements of Spectrum

frequencies = [2.407,2.412,2.417,2.422,2.427,2.432,2.437,2.442,2.447,2.452,2.457,2.462,2.467]
channels = [1,2,3,4,5,6,7,8,9,10,11]
frequencies_stats_init = [0,0,0,0,0,0,0,0,0,0,0,0,0]
Overall_channel_stats = []
Overall_frequencies_stats = []

# Real-Time Plot - Current Iteration
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111)
Ln, = ax.plot(frequencies,frequencies_stats_init, lw = 2)
ax.set_ylim(0,100)
ax.set(xlabel='Frequency (GHz)', ylabel='Busy Percentage (%)',
   title='CURRENT: WIFI Channels Busy Percentage')
plt.ion()
plt.show()

# Real-Time Plot - All Iteration
fig_All = plt.figure(figsize=(9, 7))
ax_All = fig_All.add_subplot(111)
Ln_All, = ax_All.plot(frequencies,frequencies_stats_init, lw = 2)
ax_All.set_ylim(0,100)
ax_All.set(xlabel='Frequency (GHz)', ylabel='Busy Percentage (%)',
   title='AVERAGE: WIFI Channels Busy Percentage')
plt.ion()
plt.show()

# Real-Time Plot - Channel's Busy Perc Over Time

fig_time, axs_time = plt.subplots(6, 2, figsize=(11,9))
fig_time.tight_layout(h_pad=3)
axs_time[0, 0].plot(0, 0)
axs_time[0, 0].set_ylim(0,100)
axs_time[0, 1].plot(0, 0,)
axs_time[0, 1].set_ylim(0,100)
axs_time[1, 0].plot(0, 0)
axs_time[1, 0].set_ylim(0,100)
axs_time[1, 1].plot(0, 0)
axs_time[1, 1].set_ylim(0,100)
axs_time[2, 0].plot(0, 0)
axs_time[2, 0].set_ylim(0,100)
axs_time[2, 1].plot(0, 0)
axs_time[2, 1].set_ylim(0,100)
axs_time[3, 0].plot(0, 0)
axs_time[3, 0].set_ylim(0,100)
axs_time[3, 1].plot(0, 0)
axs_time[3, 1].set_ylim(0,100)
axs_time[4, 0].plot(0, 0)
axs_time[4, 0].set_ylim(0,100)
axs_time[4, 1].plot(0, 0)
axs_time[4, 1].set_ylim(0,100)
axs_time[5, 0].plot(0, 0)
axs_time[5, 0].set_ylim(0,100)


for axss in axs_time.flat:
    axss.set(xlabel='Time', ylabel='Busy %	')

# Hide x labels and tick labels for top plots and y ticks for right plots.
#for axss in axs_time.flat:
#    axss.label_outer() 

plt.ion()
plt.show()





############################################
mean_chan_1 = []
mean_chan_2 = []
mean_chan_3 = []
mean_chan_4 = []
mean_chan_5 = []
mean_chan_6 = []
mean_chan_7 = []
mean_chan_8 = []
mean_chan_9 = []
mean_chan_10 = []
mean_chan_11 = []
mean_f1 = []
mean_f2 = []
mean_f3 = []
mean_f4 = []
mean_f5 = []
mean_f6 = []
mean_f7 = []
mean_f8 = []
mean_f9 = []
mean_f10 = []
mean_f11 = []
mean_f12 = []
mean_f13 = []

spec_file = open('spectrum_meas.txt','w')
chan_file = open('channels_meas.txt','w')

for j in range(1,max_reps+1):
	print("Iteration "+str(j))
	os.system('python file_creator.py')

	channel_stats = {}
	input_file_channel = 'channel1_bin.txt'
	output_file_channel = 'channel1_dec.txt'
	busy_prc = 0

	frequencies_stats = []
	dict_i = 1
	ann_list = []
	ann_All_list = []
	mean_chan_stats = []	# Mean stats of all channels from all iterations
	mean_freq_stats = []	# Mean stats of all frequencies from all iterations

	for i in range(1,14):
	    input_file_channel = input_file_channel.split("_")[0][:7] + str(i) + "_" + input_file_channel.split("_")[1]
	    output_file_channel = input_file_channel.split("_")[0][:7] + str(i) + "_" + output_file_channel.split("_")[1]
	    busy_prc = datamaker.file_parser(input_file_channel,output_file_channel)
	    frequencies_stats.append(busy_prc)
	    print("Frequency "+str(i)+" measured")

	
	for i in range(1,12):
		mean = (frequencies_stats[i-1] + frequencies_stats[i] + frequencies_stats[i+1])/3
		dict_index = 'Channel_' + str(i)
		channel_stats[dict_index] = round(mean,2)
		
	# Store statistics to obtain Mean from all iterations
	mean_chan_1.append(channel_stats["Channel_1"])
	mean_chan_2.append(channel_stats["Channel_2"])
	mean_chan_3.append(channel_stats["Channel_3"])
	mean_chan_4.append(channel_stats["Channel_4"])
	mean_chan_5.append(channel_stats["Channel_5"])
	mean_chan_6.append(channel_stats["Channel_6"])
	mean_chan_7.append(channel_stats["Channel_7"])
	mean_chan_8.append(channel_stats["Channel_8"])
	mean_chan_9.append(channel_stats["Channel_9"])
	mean_chan_10.append(channel_stats["Channel_10"])
	mean_chan_11.append(channel_stats["Channel_11"])
	mean_f1.append(frequencies_stats[0])
	mean_f2.append(frequencies_stats[1])
	mean_f3.append(frequencies_stats[2])
	mean_f4.append(frequencies_stats[3])
	mean_f5.append(frequencies_stats[4])
	mean_f6.append(frequencies_stats[5])
	mean_f7.append(frequencies_stats[6])
	mean_f8.append(frequencies_stats[7])
	mean_f9.append(frequencies_stats[8])
	mean_f10.append(frequencies_stats[9])
	mean_f11.append(frequencies_stats[10])
	mean_f12.append(frequencies_stats[11])
	mean_f13.append(frequencies_stats[12])

	mean_chan_stats = [round(sum(mean_chan_1)/len(mean_chan_1),2),round(sum(mean_chan_2)/len(mean_chan_2)),
						round(sum(mean_chan_3)/len(mean_chan_3),2),round(sum(mean_chan_4)/len(mean_chan_4)),
						round(sum(mean_chan_5)/len(mean_chan_5),2),round(sum(mean_chan_6)/len(mean_chan_6)),
						round(sum(mean_chan_7)/len(mean_chan_7),2),round(sum(mean_chan_8)/len(mean_chan_8)),
						round(sum(mean_chan_9)/len(mean_chan_9),2),round(sum(mean_chan_10)/len(mean_chan_10)),
						round(sum(mean_chan_11)/len(mean_chan_11),2)]

	mean_freq_stats = [sum(mean_f1)/len(mean_f1),sum(mean_f2)/len(mean_f2),
						sum(mean_f3)/len(mean_f3),sum(mean_f4)/len(mean_f4),
						sum(mean_f5)/len(mean_f5),sum(mean_f6)/len(mean_f6),
						sum(mean_f7)/len(mean_f7),sum(mean_f8)/len(mean_f8),
						sum(mean_f9)/len(mean_f9),sum(mean_f10)/len(mean_f10),
						sum(mean_f11)/len(mean_f11),sum(mean_f12)/len(mean_f12),
						sum(mean_f13)/len(mean_f13)]

	############## Plot to diagram of CURRENT iterations  ##################################################
	Ln.set_ydata(frequencies_stats)
	Ln.set_xdata(frequencies)
	plt.pause(0.001)

	for i in range(1,14):
		spec_file.write(str(frequencies_stats[i-1])+"\n")
	for i in range(1,12):
		dict_index = 'Channel_' + str(i)
		chan_file.write(str(channel_stats[dict_index])+"\n")

	print("All measurements: " , frequencies_stats)						# 13 Frequncies Measurements
	optimal_channel = min(channel_stats, key = channel_stats.get)	
	print("Channel measurements: " , channel_stats)					# 11 Channels Means (3 meas => 1 Chan)
	print("Optimal Channel: " + optimal_channel)
	
	# Plot arrows to diagram
	# Annotation 
	for k in range(1,12):
		dict_index = 'Channel_' + str(k)
		if "Channel_"+str(k) == optimal_channel: 	# Optimal Channel
			ann = ax.annotate("Channel "+str(k)+":\n"+str(channel_stats[dict_index])+"%", xy =(frequencies[k],frequencies_stats[k]+3), 
                xytext =(frequencies[k],frequencies_stats[k]+30),  
                arrowprops = dict(facecolor ='green', 
                                  shrink = 0.01),)
		else:
			ann = ax.annotate("Channel "+str(k)+":\n"+str(channel_stats[dict_index])+"%", xy =(frequencies[k],frequencies_stats[k]+3), 
                xytext =(frequencies[k],frequencies_stats[k]+10),  
                arrowprops = dict(facecolor ='red', 
                                  shrink = 0.01),)
		plt.pause(0.001)
		ann_list.append(ann)

	############## Plot to Mean diagram of All iterations  ##################################################
	Ln_All.set_ydata(mean_freq_stats)
	Ln_All.set_xdata(frequencies)
	plt.pause(0.001)

	# Plot arrows to diagram
	# Annotation 
	for k in range(1,12):
		if mean_chan_stats[k-1] == min(mean_chan_stats): 	# Optimal Channel
			ann_All = ax_All.annotate("Channel "+str(k)+":\n"+str(mean_chan_stats[k-1])+"%", xy =(frequencies[k],mean_freq_stats[k]+3), 
                xytext =(frequencies[k],mean_freq_stats[k]+30),  
                arrowprops = dict(facecolor ='green', 
                                  shrink = 0.01),)
		else:
			ann_All = ax_All.annotate("Channel "+str(k)+":\n"+str(mean_chan_stats[k-1])+"%", xy =(frequencies[k],mean_freq_stats[k]+3), 
                xytext =(frequencies[k],mean_freq_stats[k]+10),  
                arrowprops = dict(facecolor ='red', 
                                  shrink = 0.01),)
		plt.pause(0.001)
		ann_All_list.append(ann_All)
	####  Real-Time Plot - Channel's Busy Perc Over Time ############################################
	if mean_chan_stats[0] == min(mean_chan_stats) :	# optimal
		axs_time[0,0].plot([*range(len(mean_chan_1))],mean_chan_1,'tab:green')
		axs_time[0,0].set_title('Optimal Chan 1')
	else:
		axs_time[0,0].plot([*range(len(mean_chan_1))],mean_chan_1,'tab:red')
		axs_time[0,0].set_title('Channel 1')
	if mean_chan_stats[1] == min(mean_chan_stats) :	# optimal
		axs_time[0,1].plot([*range(len(mean_chan_2))],mean_chan_2,'tab:green')
		axs_time[0,1].set_title('Optimal Chan 2')
	else:
		axs_time[0,1].plot([*range(len(mean_chan_2))],mean_chan_2,'tab:red')
		axs_time[0,1].set_title('Channel 2')
	if mean_chan_stats[2] == min(mean_chan_stats) :	# optimal
		axs_time[1,0].plot([*range(len(mean_chan_3))],mean_chan_3,'tab:green')
		axs_time[1,0].set_title('Optimal Chan 3')
	else:
		axs_time[1,0].plot([*range(len(mean_chan_3))],mean_chan_3,'tab:red')
		axs_time[1,0].set_title('Channel 3')
	if mean_chan_stats[3] == min(mean_chan_stats) :	# optimal
		axs_time[1,1].plot([*range(len(mean_chan_4))],mean_chan_4,'tab:green')
		axs_time[1,1].set_title('Optimal Chan 4')
	else:
		axs_time[1,1].plot([*range(len(mean_chan_4))],mean_chan_4,'tab:red')
		axs_time[1,1].set_title('Channel 4')
	if mean_chan_stats[4] == min(mean_chan_stats) :	# optimal
		axs_time[2,0].plot([*range(len(mean_chan_5))],mean_chan_5,'tab:green')
		axs_time[2,0].set_title('Optimal Chan 5')
	else:
		axs_time[2,0].plot([*range(len(mean_chan_5))],mean_chan_5,'tab:red')
		axs_time[2,0].set_title('Channel 5')
	if mean_chan_stats[5] == min(mean_chan_stats) :	# optimal
		axs_time[2,1].plot([*range(len(mean_chan_6))],mean_chan_6,'tab:green')
		axs_time[2,1].set_title('Optimal Chan 6')
	else:
		axs_time[2,1].plot([*range(len(mean_chan_6))],mean_chan_6,'tab:red')
		axs_time[2,1].set_title('Channel 6')
	if mean_chan_stats[6] == min(mean_chan_stats) :	# optimal
		axs_time[3,0].plot([*range(len(mean_chan_7))],mean_chan_7,'tab:green')
		axs_time[3,0].set_title('Optimal Chan 7')
	else:
		axs_time[3,0].plot([*range(len(mean_chan_7))],mean_chan_7,'tab:red')
		axs_time[3,0].set_title('Channel 7')
	if mean_chan_stats[7] == min(mean_chan_stats) :	# optimal
		axs_time[3,1].plot([*range(len(mean_chan_8))],mean_chan_8,'tab:green')
		axs_time[3,1].set_title('Optimal Chan 8')
	else:
		axs_time[3,1].plot([*range(len(mean_chan_8))],mean_chan_8,'tab:red')
		axs_time[3,1].set_title('Channel 8')
	if mean_chan_stats[8] == min(mean_chan_stats) :	# optimal
		axs_time[4,0].plot([*range(len(mean_chan_9))],mean_chan_9,'tab:green')
		axs_time[4,0].set_title('Optimal Chan 9')
	else:
		axs_time[4,0].plot([*range(len(mean_chan_9))],mean_chan_9,'tab:red')
		axs_time[4,0].set_title('Channel 9')
	if mean_chan_stats[9] == min(mean_chan_stats) :	# optimal
		axs_time[4,1].plot([*range(len(mean_chan_10))],mean_chan_10,'tab:green')
		axs_time[4,1].set_title('Optimal Chan 10')
	else:
		axs_time[4,1].plot([*range(len(mean_chan_10))],mean_chan_10,'tab:red')
		axs_time[4,1].set_title('Channel 10')
	if mean_chan_stats[10] == min(mean_chan_stats) :	# optimal
		axs_time[5,0].plot([*range(len(mean_chan_11))],mean_chan_11,'tab:green')
		axs_time[5,0].set_title('Optimal Channel 11')
	else:
		axs_time[5,0].plot([*range(len(mean_chan_11))],mean_chan_11,'tab:red')
		axs_time[5,0].set_title('Channel 11')
	
	plt.pause(0.001)
	#################################################################################################
	if j != max_reps:
		print("Going to sleep...")
		time.sleep(5)
		for i, a in enumerate(ann_list):
			a.remove()
		for i, a in enumerate(ann_All_list):
			a.remove()
	else:		# End of Measurements
		fig_All.savefig("Mean_Busy_Percentage.png")
		fig_time.savefig("Channels_in_Time.png")
		print("Terminating...")
		time.sleep(10)