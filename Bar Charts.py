import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [6,7,8,1,3]

x2 = [1,3,5,7,9]
y2 = [8,8,2,4,2]
# Ceating bar charts
# add colour parameter
# matplot lib have existing colours by:
# writing the words = blues, red
# One letter colours = r : red, b : blue, k : black, c = sien
plt.bar(x, y, label ='Bars1', color = 'r')
plt.bar(x2, y2, label = 'Bars2', color = 'c')



plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting Graph\nCheck it out')

plt.legend()
plt.show()