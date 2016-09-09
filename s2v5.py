from s2v4 import *

print("\n s2v5:")

#find the max price using temporary list
def find_max(lst, col):
	temp_list = []
	for row in lst:
		item = float(row[col])
		temp_list.append(item)
	return round(max(temp_list), 2)

max_price = find_max(data_from_csv[1:], 2)
print ("\n Max price = {}".format(max_price))

#find the min price using temporary list
def find_min(lst, col):
	temp_list = []
	for row in lst:
		item = float(row[col])
		temp_list.append(item)
	return round(min(temp_list), 2)

min_price = find_min(data_from_csv[1:], 2)
print ("\n Min price = {}".format(min_price))

#find the max and min using numby ndarray
def find_max_min(lst, col, m):
	prices = data_from_numpy["priceLabel"]
	if m == "max":
		return numpy.amax(prices)
	elif m == "min":
		return numpy.amin(prices)
	else:
		pass

print ("\n Max price = {} \n\n Min price = {}".format(
		find_max_min(data_from_csv[1:], 2, "max"),
		find_max_min(data_from_csv[1:], 2, "min")
		))