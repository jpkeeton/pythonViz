#from Python Crash Course, by Eric Matthes, Chap 16
import csv
from matplotlib import pyplot as plt

#get high temps from file
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # we don't need the header row, as we're going to use the enumerate below, for a more detailed version
    # print(header_row)
# page 351
# loop thru the headers and use enumerate to get the index of each item and
# for index, column_header in enumerate(header_row):
# #     print(index, column_header)

# # page 352
#     highs = []
#     for row in reader:
#         # highs.append(row[1])
#         # now let's convert the strings to ints for matplot lib reading
#         high = int(row[1])
#         highs.append(high)
#     print(highs)

# so here i'll try to print the mean humidity
    water = []
    for row in reader:
        moist = int(row[7])
        water.append(moist)
    # print(water)

# now work on plotting it
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(water, c='red')

plt.show()



