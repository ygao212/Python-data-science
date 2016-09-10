from s3v1 import *

print("\n s3v2: ")

#filter by string condition
def filter_col_by_string(lst, field, filter_condition):
	filtered_row = []

	col = int(lst[0].index(field))
	filtered_row.append(lst[0])

	for row in lst[1:]:
		if row[col] == filter_condition:
			filtered_row.append(row)

	return filtered_row

#filter out ties of a material
silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
print("\n In total of {} ties, there are {} silk ties.".
	format(number_of_ties, number_of_records(silk_ties)))

wool_ties = filter_col_by_string(data_from_csv, "material", "_wool")
print("\n In total of {} ties, there are {} wool ties.".
	format(number_of_ties, number_of_records(wool_ties)))

cotton_ties = filter_col_by_string(data_from_csv, "material", "_cotton")
print("\n In total of {} ties, there are {} cotton ties.".
	format(number_of_ties, number_of_records(cotton_ties)))

#filter out ties of a brand
gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
print("\n In total of {} ties, there are {} Gucci ties.".
	format(number_of_ties, number_of_records(gucci_ties)))

#filter by float
def filter_col_by_float(lst, field, direction, filter_condition):
	filtered_rows = []

	col = int(lst[0].index(field))
	cond = float(filter_condition)
	filtered_rows.append(lst[0])

	for row in lst[1:]:
		item = float(row[col])

		if direction == "<":
			if item < cond :
				filtered_rows.append(row)
		elif direction == "<=":
			if item <= cond :
				filtered_rows.append(row)
		elif direction == ">":
			if item < cond:
				filtered_rows.append(row)
		elif direction == ">=":
			if item >= cond :
				filtered_rows.append(row)
		elif direction == "=":
			if item == cond :
				filtered_rows.append(row)
		else:
			pass
	return filtered_rows

#filter ties that are cheaper than 20
under_20_bucks = filter_col_by_float(data_from_csv, "priceLabel", "<=", 20)
print("\n In total of {} ties, there are {} ties under 20 bucks.".
	format(number_of_ties, number_of_records(under_20_bucks)))