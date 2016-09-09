from s2v1 import *

print("\n s2v2:")

#number of records using len() function
def number_of_records(lst):
	return len(lst) -1

number_of_ties = number_of_records(data_from_csv)

print("\n", "There are", number_of_ties, 
	"ties in our data sample, using len(list)")


#number of records using ndarray.size function
def number_of_records2(ndarray):
	return ndarray.size

number_of_ties2 = number_of_records2(data_from_numpy)

print ("\n", "There are", number_of_ties2, 
	"ties in our data sample, using ndarray.size")