import matplotlib as mpl
mpl.use('agg')

import numpy as np
import matplotlib.pyplot as plt
import pdb

def convert_data(inputs):
	result = []
	for trial in inputs:
	    error_rates = []
	    for data_point in trial:
		error_rate = float(data_point[0])/float(data_point[1])
		error_rates.append(error_rate)
		
	    result.append(erorr_rates)
		
	
	return [collectn_1, collectn_2, collectn_3, collectn_4]

def graph(data_points):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	num_packets = [1e6, 2e6, 4e6, 8e6, 16e6, 32e6]
	bp = ax.boxplot(data_points, positions=num_packets)
	fig.savefig('fig1.png')

def main():
	rhhh_accuracy_errors = [[(45,155), (15,177), (8,109), (3,99), (1,90), (1,88)]]
	data_points = convert_data()
	graph(data_points)

if __name__ == "__main__":
	main()
