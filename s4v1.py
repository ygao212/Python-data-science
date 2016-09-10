from s3v3 import *

print("\n s4v1: ")

#write list to a csv file
def write_to_file(filename, lst):
	example = csv.writer(open(filename, "w", encoding='utf-8'), dialect="excel")
	example.writerows(lst)

write_to_file("_data/s4_silk_ties.csv", silk_ties)

print("\n writting _data/s4_silk_ties.csv finished")
