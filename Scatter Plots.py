import matplotlib.pyplot as plt

x = [5.1,5,4.9,4.8,4.7,4.6,4.5,4.4,4.3,4.2,4.1,4,3.9,3.8,3.7,3.6,3.5,3.4,3.3,3.2,3.1,3,2.9,2.8,2.7,2.6,2.5,2.4,2.3,2.2]
y = [0.52,0.66,0.75,0.88,0.99,1.07,1.17,1.37,1.36,1.43,1.48,1.58,1.63,1.68,1.74,1.79,1.83,1.84,1.84,1.88,1.99,2.1,2.08,2.14,2.1,2.46,2.54,2.67,2.78,2.89]
# Creating the scatter graph
# add marker which is how the dots will be represented = *, o
# Add ther size of the markers
plt.scatter(x, y, label = 'skitscat', color = 'k', marker = '*', s = 1)
plt.xlabel('Voltage')
plt.ylabel('Resistance')
plt.title('Intereting Graph\nCheck it out')
plt.legend()
plt.show()
