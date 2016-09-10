from s4v1 import *

print("\n s4v2: ")

#a function that writes out the prand and price of a dataset
def write_brand_and_price_file(filename, lst):
	brand_field_index = 5
	price_field_index = 2

	new_array = []
	for row in lst:
		new_record = [None] * 2
		new_record[0] = row[brand_field_index]
		new_record[1] = row[price_field_index]
		new_array.append(new_record)

	write_to_file(filename, new_array)

write_brand_and_price_file('_data/s4_brand_and_price.csv', gucci_ties)
print("\n writting _data/s4_brand_and_price.csv finished")

#a function that writes out the max and min price of a dataset
def write_min_max_csv(filename, lst):
	min_val = find_min(lst, 2)
	max_val = find_max(lst, 2)

	new_array = []
	for row in lst:
		if (float(row[2]) == min_val or float(row[2]) == max_val):
			new_array.append(row)
		else:
			pass
			
	write_to_file(filename, new_array)

write_min_max_csv('_data/s4-min_max_csv.csv', gucci_ties[1:])
print("\n writting _data/s4-min_max_csv.csv finished")

#a function that write out any two colums of a dataset
def write_two_cols(filename, lst, col1, col2):
	new_array = []
	for row in lst:
		new_record = [None] * 2
		new_record[0] = row[col1]
		new_record[1] = row[col2]
		new_array.append(new_record)

	write_to_file(filename, new_array)

write_two_cols('_data/s4-write_name_description.csv', gucci_ties[1:], 3, 7)
print("\n writting _data/s4-write_name_description.csv finished")