import matplotlib.pyplot as plt


x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

# Have tro add label value
plt.plot(x,y, label = 'First line')
plt.plot(x2,y2, label = 'Second line')
# Add labels of x and y before we show graph
plt.xlabel('Plot Number')
plt.ylabel('Important var')
# Name of the graph
# Make subtitile
plt.title('interesting Graph\nCheck it out')
# Create a legend
# Legend = Name of line
plt.legend()
plt.show()