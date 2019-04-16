import numpy as np
import matplotlib.pyplot as plot
import cmath as cm
#n=input("enter length of x:")
#x=[]
'''for n in range(n):
	a=input("enter elements for x:")
	x.append(a)
print(x)'''
x=[4,3,2,-1.5,2.6,4,10,0]
n=len(x)
c=0
r=[]
w=np.linspace(-np.pi,np.pi,1000)
for i in range(1000):
	w_tem=w[i]
	j=cm.sqrt(-1)
	for l in range(0,n,1):
		c=c+(x[l]*np.exp((-(j*w_tem*l))))
	r.append(c)
	c=0
g=np.abs(r)
h=np.angle(r)
plot.subplot(311)
plot.plot(w,r)
plot.subplot(312)
plot.plot(w,g)
plot.subplot(313)
plot.plot(w,h)
plot.show()
		
