import matplotlib.pyplot as plt
# http://blog.adnansiddiqi.me/data-visualization-in-python-pie-charts-in-matplotlib/

# x = [2, 4, 6]
# y = [1, 3, 5]
# plt.plot(x, y)
# plt.show()

Year = [1970, 1980, 1990, 2000, 2010]
Pork = [55.4, 56.8, 49.4, 50.8, 47.2]
Beef = [84.4, 76.4, 67.5, 67.5, 59.4]
Chicken = [36.6, 45.8, 59.5, 77, 82.4]
Fish = [11.8, 12.5, 15, 15.2, 15.8]


plt.plot(Year, Pork, color='tan')
plt.plot(Year, Beef, color='red')
plt.plot(Year, Chicken, color='blue')
plt.plot(Year, Fish, color='green')
plt.xlabel('Decade')
plt.ylabel('Pounds Eaten')
plt.title('U.S. Per Capita Meat Consumption - 1970 - 2010')
plt.show()
