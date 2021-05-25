import numpy as np  
import scipy as sc
from statistics import *


def file_parser(input_file , output_file):
	dec_file = open(output_file,'w')
	total_values = 0
	over_minus_20 = 0
	counter = 0
	fft_size = 50
	mean_dec_file = open('mean_' + input_file,'w')
	
	f = sc.fromfile(open(input_file), dtype=sc.int8)
	#print(len(f))
	cur_sum=0;
	for i in range(0,len(f)):
		#dec_file.write(str(f[i]))
		cur_sum = cur_sum + f[i]
		#print(f[i])
		if i%fft_size == 0:
			total_values = total_values +1;
			mean = cur_sum/fft_size
			#mean_dec_file.write(str(mean)+"\n")
			cur_sum=0;
			if mean > -20:
				over_minus_20 = over_minus_20 + 1;
		busy_per = over_minus_20/total_values
		busy_per = round(busy_per*100,2)
	return(busy_per)