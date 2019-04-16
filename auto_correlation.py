import numpy as np
import matplotlib.pyplot as plot
n=input("enter length of x elements")
x=[]
r=[]
h=[]
k=n
f=n+k-1
for i in range(n):
	a=input("enter elements for x")
	x.append(a)
print(x)
for i in range(k):
	e=x[n-i-1]
	h.append(e)
print(h)
c=0
while k<f:
	h.append(0)
	k=k+1
for i in range(f):
	for j in range(n):
		c=c+((x[j])*(h[i-j]))
	r.append(c)
	c=0  
print r
s=np.arange(0,f,1)
plot.stem(s,r)
plot.show()
	

