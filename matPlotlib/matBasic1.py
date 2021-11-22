import matplotlib.pyplot as plt
import numpy as np 
x=np.arange(-4,4,.1)
y=np.square(x)
y2=x*x+2
y3=x*x-2
plt.grid(True)
plt.xlabel('My x values')
plt.ylabel('My y values')
plt.title('My first graph')
#plt.axis([0,5,0,10])
plt.plot(x,y,"b-*",linewidth=3,markersize=7,label='Blue Line')
plt.plot(x,y2,"r-*",linewidth=3,markersize=7,label='Blue Line')
plt.plot(x,y3,"g-*",linewidth=3,markersize=7,label='Blue Line')
plt.legend(loc='upper center')
plt.show()


#kill the graph before you run another
