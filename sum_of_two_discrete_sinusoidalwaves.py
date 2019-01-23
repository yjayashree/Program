import numpy as np
import matplotlib.pyplot as plot
f1=input("enter first frequency")
f2=input("enter second frequency")
fs=input("enter sampling frequency")
n=np.arange(0,100,1);
x1=np.cos(2*(3.14)*(f1/fs)*n)
x2=np.cos(2*(3.14)*(f2/fs)*n)
x=x1+x2
plot.subplot(3,1,1)
plot.plot(n,x1)
plot.subplot(3,1,2)
plot.plot(n,x2)
plot.subplot(3,1,3)
plot.plot(n,x)
plot.show()


