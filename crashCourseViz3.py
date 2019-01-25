#from Python Crash Course, by Eric Matthes, Chap 16
import csv
from matplotlib import pyplot as plt
from datetime import datetime

#get high temps from file
# filename = 'sitka_weather_07-2014.csv'
filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# page 357
    dates, highs, lows = [], [], []
    for row in reader:
        #here we'll add the dates
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # highs.append(row[1])
        # now let's convert the strings to ints for matplot lib reading
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
    print(highs)

#Here let's plot the data
fig = plt.figure(dpi=128, figsize=(10,6))
# alpha controls the color's transparency
plt.plot(dates, highs, c='red', alpha=0.9)
plt.plot(dates, lows, c='blue', alpha=0.9)
# page 358, shading an area chart
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)



#format the plot
# plt.title("Daily high temperatures, July 2014", fontsize=24)
#this line, fig.autofmt.. puts diagonally to prevent overlap
fig.autofmt_xdate()
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#display the plot
plt.show()
