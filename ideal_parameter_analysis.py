import numpy as np
import matplotlib.pyplot as plt
k=1.38e-23
T=300
q=1.602e-19
Io=1e-10
n=1
Iph=np.array([0.030, 0.09, 0.15])  # Photocurrent values for different light intensities
V=np.linspace(0,0.6,1000)
results=[]
for Iph in Iph:
    I_ideal= Iph-Io*(np.exp(q*V/(k*T))-1)
    Isc=I_ideal[0]
    print("Iph=",Iph)
    print("Isc=",Isc)
    Voc_ind=np.argmin(np.abs(I_ideal))
    Voc=V[Voc_ind]
    print("Voc=",Voc)
    P=I_ideal*V
    Pmax=np.max(P)
    print("Maximum Power:",Pmax)
    ind=np.argmax(P)
    Vmp=V[ind]
    Imp=I_ideal[ind]
    print("Imp:",Imp)
    print("Vmp:",Vmp)
    FF=Pmax/(Voc*Isc)
    print("Fill factor:",FF)
    results.append((Iph, Isc, Voc, Imp, Vmp, Pmax, FF))
    plt.plot(V,I_ideal,label='Ideal I-V Curve for Iph={}'.format(Iph))
plt.xlabel('Voltage(X)')
plt.ylabel('Current(Y)')
plt.grid()
plt.legend()
plt.title("I-V Curve of Solar Cell")
plt.show()
np.savetxt("ideal_parameter_results.csv", results, header='Iph\tIsc\tVoc\tImp\tVmp\tPmax\tFF', fmt='%1.5f', delimiter='\t')
