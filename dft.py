import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
def dft(x,N):
	c=0
	r=[]
	for k in range(N-1):
		j=cm.sqrt(-1)
		for l in range(0,N-1,1):
			c=c+(x[l]*np.exp((-(j*2*np.pi*k*l/N))))
		r.append(c)
		c=0
	return r
x=[4,3,2,-1.5,2.6,4,10,1,15]
N=len(x)
n=np.arange(0,N-1,1)
m=input("enter n point dft:")
t=m-N
y=[]
while(t>=0):
	x.append(0)
	t=t-1
y.append(x)
print(y)
v=dft(x,N)
u=dft(y,m)
g1=np.abs(v)
h1=np.angle(v)
g2=np.abs(u)
h2=np.angle(u)
plot.subplot(231)
plot.plot(v)
plot.subplot(234)
plot.plot(u)
plot.subplot(232)
plot.plot(g1)
plot.subplot(235)
plot.plot(g2)
plot.subplot(233)
plot.plot(h1)
plot.subplot(236)
plot.plot(h2)
plot.show()
		
