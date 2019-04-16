import numpy as np
import matplotlib.pyplot as plot
n=input("enter length of x elements")
k=input("enter length of h elements")
x=[]
r=[]
h=[]
z=[]
f=n+k-1
for i in range(n):
	a=input("enter elements for x")
	x.append(a)
print(x)
for i in range(k):
	b=input("enter elements for h")
	h.append(b)
print(h)
for i in range(k):
	e=h[k-i-1]
	z.append(e)
print(z)
c=0
while k<f:
	z.append(0)
	k=k+1
for i in range(f):
	for j in range(n):
		c=c+((x[j])*(z[i-j]))
	r.append(c)
	c=0  
print r
s=np.arange(0,f,1)
plot.stem(s,r)
plot.show()
	

