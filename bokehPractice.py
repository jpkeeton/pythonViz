# #Import library
# from bkcharts import Bar, output_file, show
# #use output_notebook to visualize it in notebook
#
# # prepare data (dummy data)
# data = {"y": [1, 2, 3, 4, 5]}
#
#
# # Output to Line.HTML
# output_file("lines.html", title="line plot example") #put output_notebook() for notebook
#
# # create a new line chat with a title and axis labels
# p = Bar(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)
#
# # show the results
# show(p)


# this one works

# from bokeh.plotting import figure, output_file, show
#
# # prepare some data
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
#
# # output to static HTML file
# output_file("lines.html", title="line plot example")
#
# # create a new plot with a title and axis labels
# p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
#
# # add a line renderer with legend and line thickness
# p.line(x, y, legend="Temp.", line_width=2)
#
# # show the results
# show(p)



# this is my attempt to redo the Meat Consumption Viz for MakeoverMonday
# http://bokeh.pydata.org/en/latest/docs/user_guide/quickstart.html#userguide-quickstart

from bokeh.plotting import figure, output_file, show
output_file("test.html")
p = figure()
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)
show(p)

# <><><><><><<>

# # this is matplolib
# import matplotlib.pyplot as plt;
#
# plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
#
# objects = ('Stanford', 'Washington', 'Penn State', 'Nebraska', 'Hawaii', 'UCLA')
# y_pos = np.arange(len(objects))
# performance = [1, 8, 15, 12, 7, 9]
#
# plt.bar(y_pos, performance, align='center', alpha=0.9)
# plt.xticks(y_pos, objects)
# plt.ylabel('Wins')
# plt.title('NCAA Women\'s Volleyball Champs')
#
# plt.show()
# # plt.