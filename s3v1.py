from s2v5 import *

print("\n s3v1: ")

#add new attribute cashmere or not
def create_bool_field_from_search_term(lst, search_term):
	new_array = []
	new_header = lst[0][:]
	new_header.append(search_term)
	new_array.append(new_header)

	for row in lst[1:]:
		new_bool = False
		if search_term in row[7]:
			new_bool = True
		row.append(new_bool)
		new_array.append(row)

	return new_array

add_cashmere_bool = create_bool_field_from_search_term(data_from_csv, "cashmere")

#filter if made of cashmere (boolean)
def filter_by_bool(lst, col):
	matches_search_term = []

	for row in lst[1:]:
		if row[col]:
			matches_search_term.append(row)

	return matches_search_term


col_of_search_term = add_cashmere_bool[0].index("cashmere")	

filter_cashmere = filter_by_bool(add_cashmere_bool, col_of_search_term)

num_cashmere = number_of_records(filter_cashmere)

print("\n In total of {} ties, there are {} ties made of cashmere.".
	format(number_of_ties, num_cashmere))