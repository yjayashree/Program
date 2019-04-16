import numpy as np
from matplotlib import pyplot as plt
b=[]
c=[]
x=0
k=input("enter length")
for i in range(int(k)):
	a=input("eneter inputs")
	b.append(a)
	x=x+a
	c.append(x)
n=np.arange(0,k,1)
plt.stem(n,c)
plt.show()

