from s2v2 import *

print("\n s2v3:")

#calculate total value using for loop in a list
def calculate_sum_for_loop(lst):
	total = 0
	for row in lst[1:]:
		price = float(row[2])
		total += price
	return round(total,2)

print("\n Total value of ties is {}, using lst for loop".
	format(calculate_sum_for_loop(data_from_csv)))


#calculate total value using sum function
def calculate_sum_sum_function(lst):
	price = [float(row[2]) for row in lst[1:]]
	return round(sum(price), 2)

print("\n Total value of ties is {}, using lst sum function".
	format(calculate_sum_sum_function(data_from_csv)))


#calculate total value using map lambda
def calculate_sum_map_lambda(lst):
	price = list(map(lambda row: float(row[2]) , lst[1:]))
	return round(sum(price), 2)
print("\n Total value of ties is {}, using lst map lambda function".
	format(calculate_sum_map_lambda(data_from_csv)))


#calculate total value using numpy sum
def calculate_sum_numpy_sum(ndarray):
	price = ndarray['priceLabel']
	float_price = [float(line) for line in price]
	total = round(numpy.sum(float_price),2)
	return total
print("\n Total value of ties is {}, using ndarray numpy.sum function".
	format(calculate_sum_numpy_sum(data_from_numpy)))