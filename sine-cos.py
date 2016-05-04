import matplotlib.pylab as pl
import numpy as np

x = np.linspace(-np.pi,np.pi,100)
y = pl.sin(x)
z = pl.cos(x)
pl.plot(x,y,'r+',x,z,'k*') #import plot from pylab as pi and plot.
pl.xlabel('time')
pl.ylabel('value')
pl.title('trogonometric data of $Sine(x)$ and $Cos(x)$')
pl.show() #show the plot

