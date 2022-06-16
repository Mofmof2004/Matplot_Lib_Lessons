import matplotlib.pyplot as plt
# when importinfg files have to use numpy or csv
import csv

x = []
y = []

# Open file
with open('Tuto_7.txt') as csvfile:
    # plots = the csvfile
    # delimeter is what will seperate the values in the file
    plots = csv.reader(csvfile, delimiter = ',')
#         adding the values in the x list
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
# Creating a graph with the info from the file
plt.plot(x, y, label = 'Loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intereting Graph\nCheck it out')
plt.legend()
plt.show()


# More popular way is to use numpy
import numpy as np

# use numpy to load file and unpack the file using x and y
# unpack will load the file and directly add the info into the x and y list as info in txt is = 1:2
# only work as there are 2 variables
x, y = np.loadtxt('Tuto_7.txt', delimiter=',', unpack=True )
plt.plot(x, y, label = 'Loaded from file')