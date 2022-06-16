import matplotlib.pyplot as plt
# Bring in the animation functionality
import matplotlib.animation as animation
# Use to make the graph look more appealing for the viewer
from matplotlib import style

# use a style for the graph
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# create a function for animation of the graph
def animate(i):
    # open file and intention to read = 'r' and read
    graph_data = open('Tuto_7.txt', 'r').read()
    # splitting each line with a blank line
    lines = graph_data.split('\n')
#     creating x list and y
    xs = []
    ys = []
    # looping for each lines
    for line in lines:
        # to make sure that the line is not empty by ignoring it
        if len(line)>1:
            # split line with a coma
            x, y = line.split(',')
#             add the info in lists

            xs.append(float(x))
            ys.append(float(y))
#     clear all data
    ax1 .clear()
# plotting in the graph
    ax1.plot(xs, ys)
#Funcanimation means that we will base animation on a function
# where will we animate, what is the function that we will animate, any parameter = intervals is in millimeters, so says that every seconds this graph will update
ani = animation.FuncAnimation(fig, animate, interval=1000)
# show the new graph
plt.show()