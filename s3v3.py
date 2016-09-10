from s3v2 import *

print("\n s3v3: ")

#max price grouping by brand
gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max_min(jcrew_ties[1:], 2, "max")

message = "\n {} {} tie price is ${:03.2f}"
print(message.format("Maximum", "Gucci", max_gucci))
print(message.format("Maximum", "J.Crew", max_jcrew))

#average price 
avg_gucci = find_average(gucci_ties[1:], True)
avg_jcre = find_average(jcrew_ties[1:], True)

print(message.format("Average", "Gucci", avg_gucci))
print(message.format("Average", "J.Crew", avg_gucci))

#
striped_ties = filter_col_by_string(data_from_csv, "print", "_striped")
print_ties = filter_col_by_string(data_from_csv, "print", "_print")
paisley_ties = filter_col_by_string(data_from_csv, "print", "_paisley")
solid_ties = filter_col_by_string(data_from_csv, "print", "_solid")

message = "{}\t${:03.2f}"
print("\nPrint\tAverage".expandtabs(30))

for type_of_tie in (striped_ties, print_ties, paisley_ties, solid_ties):
	print(message.format(type_of_tie[1][9], find_average(type_of_tie[1:])).expandtabs(30))