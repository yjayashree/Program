import numpy as np
import matplotlib.pyplot as plot
f=20
fs=2000
n=np.arange(0,200,1)
am=np.cos(2*np.pi*f*n/fs)
b=np.random.rand(am.shape[0])
c=am+b
p=input("enter order of system")
x=0
y=[]
for i in range(0,200,1):
	for j in range(0,int(p)-1,1):
		x=x+c[i-j]
		print(x)
	z=float((x)/(p))
	y.append(z)
	x=0
plot.subplot(411)
plot.plot(n,am)
plot.subplot(412)
plot.plot(n,b)
plot.subplot(413)
plot.plot(n,c)
plot.subplot(414)
plot.plot(n,y)
plot.show()
