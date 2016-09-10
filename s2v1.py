import csv
import numpy

print("\n s2v1:")

#load with csv.reader
def open_with_csv(filename, d):
	data = []
	with open(filename, encoding='utf-8') as tsvin:
		tie_reader = csv.reader(tsvin, delimiter=d)
		for line in tie_reader:
			data.append(line)
	return data

data_from_csv = open_with_csv('data.csv', "\t")
print("\n data sample: {}, and it's in {} datatype".
	format(data_from_csv[0], type(data_from_csv)))


#load with numpy genfromtxt
FIELDNAMES = [
			'',
			'id',
			'priceLabel',
			'name',
			'brandId',
			'brandName',
			'imageLink',
			'desc',
			'vendor',
			'patterned',
			'material'
			]

DATATYPES = [
			('','i'),
			('id','i'),
			('priceLabel','f8'),
			('name','a200'),
			('brandId','<i8'),
			('brandName','a200'),
			('imageLink','|S500'),
			('desc','|S900'),
			('vendor','|S100'),
			('pattern','|S50')
			]

def load_data(filename, d):
	my_csv = numpy.genfromtxt(
							filename, 
							delimiter=d, 
							skip_header=1, 
							invalid_raise=False,
							names=FIELDNAMES,
							dtype=DATATYPES
							)
	return my_csv

data_from_numpy = load_data('data.csv', '\t')
print("\n data sample: {}, and it's in {} datatype".
	format(data_from_numpy[0], type(data_from_numpy)))