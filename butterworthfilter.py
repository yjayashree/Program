import numpy as np
from matplotlib import pyplot as plot
mp=1/((2)**0.5)
ms=0.01
wp=1000*np.pi
ws=2000*np.pi
def butterworth(mp,ms,wp,ws):
	n=float(0.5*(np.log(((1/(mp)**2)-1)/((1/(ms)**2)-1))/(np.log(wp/ws))))
	N=np.ceil(float(n))
	wc=float(wp/(((1/(mp)**2)-1)**(1/(2*N))))
	w=np.arange(0,1000,1)
	h=[]
	for w in range(1000):
		e=1/((1+(w/wc)**(2*N))**(0.5))
		h.append(e)
 	return N,wc,h
Nb,wc,h=butterworth(mp,ms,wp,ws)
print Nb,wc
plot.plot(h)
plot.show()
'''def chebyshev(mp,ms,wp,ws):
	a=((1/(mp)**2)-1)
	b=((1/(ms)**2)-1)
	e=np.sqrt(a)
	N=np.ceil(np.arccosh((1/e)*(np.sqrt(b)))/(np.arccosh(ws/wp)))
	return N,e
Nb,wc=butterworth(mp,ms,wp,ws)
print Nb,wc
Nc,e=chebyshev(mp,ms,wp,ws)
print Nc,e
hc=[]
for w in range(1000)
	if('''



