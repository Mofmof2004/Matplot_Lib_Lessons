import matplotlib.pyplot as plt


days = [1,2,3,4,5]


sleeping = [7,8,6,11,7]
eating =  [2,3,4,3,2]
working = [7,8,7,2,2]
# playing = [8,5,7,8,13]
#  writing pies slices varaible = how the pie will be sliced
slices = [7,2,2,13]
# Writing all the activities
activities = ('sleeping', 'eating', 'working', 'playing')
# Writing the colours
cols = ['c','m','r','b']
# creating the pie
# add the start angle of the pie slices
# Can add shadow to the pie = shadow
# Can pull out a piece of pie = explode
# exploding eating
# add the percentage to the pie = autopct , dw about what %1.1f%%, just how to add percentage
plt.pie(slices, labels= activities, colors=cols, startangle= 90, shadow=True, explode=(0, 0.1,0,0), autopct= '%1.1f%%')

plt.title('Intereting Graph\nCheck it out')
plt.show()