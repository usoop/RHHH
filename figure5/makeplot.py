#!/usr/local/bin/ipython -pylab
import pdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

f = open('trace_chicago2016.summary', 'rU').read().strip().split('\n')
g = [[tuple(s.split('=')) for s in r.split()] for r in f]
import tabular as tb
x = tb.tabarray(kvpairs = g)
x.saveSV('anything.tsv')
y = tb.tabarray(SVfile='anything.tsv')

#directory to save images in
directory='./'
#extension/file type (eps/png/pdf/ps/svg)
extension='.png'

value = "time"
plt.figure()
algnames = ['./ancestry2', './full2', './RandHHH2D', './10RandHHH2D']
markers = ['+','x','*', 'o']
for i in range(len(algnames)):
	ind = (y['algorithm']==algnames[i]) & (y['nitems']==3000000) & (y['counters']<=10000)
	ind2 = y['counters'][ind].argsort()
	plt.plot(1.0/y['counters'][ind][ind2], 3.0/y[value][ind][ind2], marker=markers[i])
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('$\\varepsilon$', fontsize=12)
plt.xscale('log', basex=2)
plt.ylabel('Updates per Second (Millions)', fontsize=12)
plt.title('Byte-granularity in two dimensions with $N=3$ million', fontsize=12)
plt.legend(['Partial Ancestry','Full Ancestry', 'RandHHH', '10-RandHHH'])
plt.savefig(directory + 'veps'+ value+  extension)
plt.close()
quit()

