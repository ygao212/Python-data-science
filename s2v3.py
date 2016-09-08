from s2v2 import *

def calculate_sum(data_sample):
	total = 0
	for row in data_sample[1:]:
		price = float(row[2])
		total += price
	return total

print("total value of ties is {}".format(calculate_sum(data_from_csv)))