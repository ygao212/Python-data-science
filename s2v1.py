import csv
import numpy

def open_with_csv(filename):
	data = []
	with open(filename, encoding='utf-8') as tsvin:
		tie_reader = csv.reader(tsvin, delimiter='\t')
		for line in tie_reader:
			data.append(line)
		return data

data_from_csv = open_with_csv('data.csv')

