import pdb
import re

def parse_file(filename):
	results_by_packet_number = {}
	current_trial = 0
	with open(filename) as f:
	    while True:
		line = f.readline()
		if not line:
		    break
		if line.startswith("Trial"):
		    current_trial = line.split()[1]
		elif " pairs took " in line:
		    line_tokens = line.split()
		    result_obj = {}
		    num_packets = int(line_tokens[0])
		    if num_packets not in results_by_packet_number:
			results_by_packet_number[num_packets] = []
		    result_obj["time"] = line_tokens[3]
		    result_obj["trial"] = current_trial
		    result_obj["num_reported_hhh"] = line_tokens[-2]
		    line2 = f.readline()	
		    accErrors, covErrors, exactHHH = re.match('([0-9]+)\saccErrors\s([0-9]+)\scovErrors\s([0-9]+)\sexact\shhhs\n', line2).group(1, 2, 3)
		    result_obj["accuracy_errors"] = accErrors
		    result_obj["coverage_errors"] = covErrors
		    result_obj["num_exact_hhh"] = exactHHH
		    results_by_packet_number[num_packets].append(result_obj)
	return results_by_packet_number

def main():
	filename = "trace_chicago2015_RandHHH2D_output.txt"
	result = parse_file(filename)
	print result

if __name__ == "__main__":
	main()
