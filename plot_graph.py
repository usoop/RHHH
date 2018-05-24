import matplotlib as mpl
mpl.use('agg')

import numpy as np
import matplotlib.pyplot as plt
import pdb
from parse_results import parse_file

import scipy as sp
import scipy.stats

def extract_accuracy_error_rates(results_obj):
	packet_num_to_accuracy = {}
	for packet_num in results_obj:
	    error_rates = []
	    for trial in results_obj[packet_num]:
		accuracy_errors = trial["accuracy_errors"]
		num_hhh = trial["num_reported_hhh"]
		error_rates.append(float(accuracy_errors)/float(num_hhh))
	    packet_num_to_accuracy[packet_num] = confidence_interval_95(error_rates)
	return packet_num_to_accuracy

def extract_coverage_error_rates(results_obj):
	packet_num_to_coverage = {}
	for packet_num in results_obj:
	    error_rates = []
	    for trial in results_obj[packet_num]:
		coverage_errors = trial["coverage_errors"]
		num_exact_hhh = trial["num_exact_hhh"]
		error_rates.append(float(coverage_errors)/float(num_exact_hhh))
	    packet_num_to_coverage[packet_num] = confidence_interval_95(error_rates)
	return packet_num_to_coverage

def graph(rhh_confidence_intervals, _10_rhh_confidence_intervals):
	x_val = [rhh_confidence_intervals.keys(), _10_rhh_confidence_intervals.keys()]
	intervals = [rhh_confidence_intervals.values(), _10_rhh_confidence_intervals.values()]
	y_val = [[], []]
	y_err = [[], []]
	for i in range(len(intervals)):
	    for interval in intervals[i]:
	        y_val[i].append((interval[0]+interval[1])/2)
	        y_err[i].append((interval[1]-interval[0])/2)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	bp = ax.errorbar(x_val[0], y_val[0], yerr=y_err[0], color="red", marker='o', capsize=10, ls="none")
	bp = ax.errorbar(x_val[1], y_val[1], yerr=y_err[1], color="blue", marker='o', capsize=10, ls="none")
	fig.savefig('accuracy_error_fig.png')

# Uses the student t distribution to compute a 95% confidence interval
# @param data
#    A list of data points for which we want to compute the confidence interval
# @return
#    A tuple (x, y) representing the lower and upper bounds of the computed interval
def confidence_interval_95(data):
        a = 1.0*np.array(data)
        n = len(a)
        m, se = np.mean(a), scipy.stats.sem(a)
        h = se * sp.stats.t._ppf((1+.95)/2., n-1)
        return (m-h, m+h)
        
def main():
	rhhh_results = parse_file("trace_chicago2015_RandHHH2D_output.txt")
	_10_rhhh_results = parse_file("trace_chicago2015_10RandHHH2D_output.txt")

	accuracy_error_rates = extract_accuracy_error_rates(rhhh_results)
	coverage_error_rates = extract_coverage_error_rates(rhhh_results)
	_10_accuracy_error_rates = extract_accuracy_error_rates(_10_rhhh_results)
	_10_coverage_error_rates = extract_coverage_error_rates(_10_rhhh_results)

	graph(accuracy_error_rates, _10_accuracy_error_rates)

if __name__ == "__main__":
	main()
