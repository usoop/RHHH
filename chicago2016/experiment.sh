#!/bin/bash

traces=("trace_chicago2016")
algs=('RandHHH2D' '10RandHHH2D')
num_packets=(1000000 2000000 4000000 8000000 16000000 32000000)
trials=(1 2 3 4 5)

for trial in ${trials[@]}; do
	echo "Starting Trial ${trial}"
	for trace_file in ${traces[@]}; do
	    for alg in ${algs[@]}; do
		result_file=${trace_file}_${alg}_output.txt
		echo "Trial ${trial}" >> ${result_file}
		for packet_num in ${num_packets[@]}; do
		    threshold=$((${packet_num} / 100))
		    temp_out_file=TwoD_Bytes_${trace_file}_${alg}_${packet_num}.out
		    echo "(H=25). ${packet_num} packets, 1000 counters per hierarchy node, ${threshold} packets threshold."
		    ../${alg} ${packet_num} 1000 ${threshold} ${temp_out_file} < $trace_file >> ${result_file}
		    ../check2 ${trace_file} ${temp_out_file} | tail -1 >> ${result_file}
		    rm ${temp_out_file}
		done
	    done
	done
done
