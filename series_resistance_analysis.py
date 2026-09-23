import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
k=1.38e-23
T=300
q=1.602e-19
Io=1e-10
n=1
Rs=np.array([0.5,1.5,2.5,3.5])  # Series resistance values
Rsh=1000  # Shunt resistance value
V=np.linspace(0,0.6,1000)
results=[]
Iph=0.030  # Photocurrent value
def solar_equation(I_real,V,R):
    return I_real-Iph+Io*(np.exp(q*(V+I_real*R)/(n*k*T))-1)+(V+I_real*R)/Rsh
for R in Rs:
    I_real=[]
    for v in V:
     i=brentq(solar_equation,-2,2,args=(v,R))
     I_real.append(i)
    I_real=np.array(I_real)
    print("Rs=",R)
    Isc=I_real[0]
    print("Isc=",Isc)
    Voc_ind=np.argmin(np.abs(I_real))
    Voc=V[Voc_ind]
    print("Voc=",Voc)
    P=I_real*V
    Pmax=np.max(P)
    print("Maximum Power:",Pmax)
    ind=np.argmax(P)
    Vmp=V[ind]
    Imp=I_real[ind]
    print("Imp:",Imp)
    print("Vmp:",Vmp)
    FF=Pmax/(Voc*Isc)
    print("Fill factor:",FF)
    plt.plot(V,I_real,label='Real I-V Curve for Rs={}'.format(R))
    results.append((R, Isc, Voc, Imp, Vmp, Pmax, FF))

np.savetxt("series_resistance_results.csv", results, header='Rs\tIsc\tVoc\tImp\tVmp\tPmax\tFF', fmt='%1.5f', delimiter='\t')
plt.xlabel('Voltage(X)')
plt.ylabel('Current(Y)')
plt.grid()
plt.legend()
plt.title("I-V Curve of Solar Cell")
plt.show()
