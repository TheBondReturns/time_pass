# FOURIER TRANSFORM VISUALIZED

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x)*np.cos(x)
def g(x,w):
    return f(x)*np.cos(w*x)
def h(x,w):
    return f(x)*np.sin(-w*x)
def reFT(w):
    return scipy.integrate.quad(g,0,+np.inf,args=(w,))
def imFT(w):
    return scipy.integrate.quad(h,0,+np.inf,args=(w,))

blst=np.linspace(-10,10,202)
reFTlst=[]
imFTlst=[]
for w in blst:
    reFTlst.append(reFT(w))
    imFTlst.append(imFT(w))
for i in range(len(reFTlst)):
    reFTlst[i]=reFTlst[i][0]
    imFTlst[i]=imFTlst[i][0]  
    
    
plt.plot(blst,reFTlst,label="Real part")
plt.plot(blst,imFTlst,label="Imaginary part")
plt.hlines(0,-10,10,linestyle='dashed',linewidth=0.7)
plt.vlines(0,-0.6,0.6,linestyle="dashed",color="black",linewidth=0.5)
plt.xlabel("w",loc="right")
plt.title("Fourier transform of e^(-x) cos(x), visualized")
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend()
plt.show()
