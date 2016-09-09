from s2v3 import *

print("\n s2v4:")

#find average using list total / size
def find_average(lst, header=False):
	if header:
		lst = lst[1:]
	total = calculate_sum_for_loop(lst)
	size = number_of_records(lst)
	average = total / size
	return round(average, 2)

average_price = find_average(data_from_csv, True)
print("\n Average = {:03.2f}, using list total / size".format(average_price))


#find midpoint
midpoint = round(number_of_ties / 2)

#find the average of the first half of data
first_half_average = find_average(data_from_csv[:midpoint], True)

#fidn the average of the second half of data
second_half_average = find_average(data_from_csv[midpoint:], False)

print("\n The average of the first half = {}".format(first_half_average))
print("\n The average of the second half = {} ".format(second_half_average))