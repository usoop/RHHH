import matplotlib as mpl
mpl.use('agg')

import numpy as np
import matplotlib.pyplot as plt

def convert_data():
	np.random.seed(10)
	collectn_1 = np.random.normal(100, 10, 200)
	collectn_2 = np.random.normal(80, 30, 200)
	collectn_3 = np.random.normal(90, 20, 200)
	collectn_4 = np.random.normal(70, 25, 200)

	return [collectn_1, collectn_2, collectn_3, collectn_4]

def graph(data_points):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	bp = ax.boxplot(data_points)
	fig.savefig('fig1.png')

def main():
	data_points = convert_data()
	graph(data_points)

if __name__ == "__main__":
	main()
