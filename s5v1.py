from s4v3 import *
import matplotlib.pyplot as plt

print("\n s5v1: ")

#create line chart of prices and numbers of ties
def create_line_chart(lst, title, exported_figure_filename):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	prices = (sorted(map(float, lst)))

	x_axis_ticks = list(range(len(lst)))
	ax.plot(x_axis_ticks, prices,  linewidth=2)
	ax.set_title(title)
	ax.set_xlim([0, len(lst)])
	ax.set_xlabel('Tie Price ($)')
	ax.set_ylabel('Number of Ties')

	fig.savefig(exported_figure_filename)

create_line_chart([x[2] for x in gucci_ties[1:]], "Distribution of Prices for Gucci Ties",
	"_charts/s5-line-gucci.png")
print("\n saving chart _charts/s5-line-gucci.png finished")