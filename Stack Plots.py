import matplotlib.pyplot as plt


days = [1,2,3,4,5]

# All activities during the day
sleeping = [7,8,6,11,7]
eating =  [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

# Not able to label the different colours, so here is other way to do:
# By creating labels + change line width
plt.plot([],[], color = 'm', label='Sleeping', linewidth = 5 )
plt.plot([],[], color = 'c', label='Eating', linewidth = 5 )
plt.plot([],[], color = 'r', label='Working', linewidth = 5 )
plt.plot([],[], color = 'k', label='Playing', linewidth = 5 )

# creating a stacck plot
plt.stackplot(days, sleeping, eating,working, playing, colors = ['m','c','r','k'])


plt.xlabel('x')
plt.ylabel('y')
plt.title('Intereting Graph\nCheck it out')
plt.legend()
plt.show()
