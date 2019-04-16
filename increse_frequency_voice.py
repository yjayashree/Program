import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('my.wav')
print(fs)
t1=np.arange(0,len(data)/fs,1.0/fs)
print(data)
#plt.plot(t1,data[0:len(t1)])
plt.plot(data)
plt.show()
wav.write('slow.wav',(0.01)*fs,data)


