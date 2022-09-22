
import read, amrplot, os
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import matplotlib
matplotlib.use('AGG')


kl=int(argv[1]) #number of the file to plot 


D=read.loadvti(kl,file='collapse/data_d3_l3_n')
      #define X (it's the same for all files)
X=np.exp(D.x)-1.
PT=D.ptav[:,31]
PD=D.pdav[:,31]
PM=D.pmav[:,31]
TM=D.tmav[:,31]
CTHH=D.cthhav[:,31]
CTHM=D.cthmav[:,31]
CPHH=D.cphhav[:,31]
CPHM=D.cphmav[:,31]
GR=D.grav[:,31]
TOTAL=PT+PD+PM+TM+CTHH+CTHM+CPHH+CPHM+GR
uPhi=D.uPHI[:,31]
ut=D.u0[:,31]
rh=D.rho[:,31]
v4=D.vol4[:,31]



#plot without avgs

fig1, (ax1, ax2) = plt.subplots(2,1,figsize=(9,12))

#1st plot 
ax1.plot(X[::4],PT[::4],'-+',label="Thermal pressure")              #thermal pressure 
ax1.plot(X[::4],PD[::4],label="Dynamic pressure")               #Dynamic pressure
ax1.plot(X[::4],PM[::4]+TM[::4],'-*',label="Magnetic pressure")      #magnetic pressure
ax1.plot(X[::4],CTHH[::4]+CTHM[::4],'-x',label=r"Centrifugal $\theta$")      #centrifugal theta
ax1.plot(X[::4],CPHH[::4]+CPHM[::4],'-_',label=r"Centrifugal $\phi$")      #centrifugal phi
ax1.plot(X[::4],GR[::4],'-.',label="Gravity")               #gravity
ax1.plot(X[::4],PT[::4]+PD[::4]+PM[::4]+TM[::4]+CTHH[::4]+CTHM[::4]+CPHH[::4]+CPHM[::4]+GR[::4],'--', label ="Total") #total
ax1.legend(loc="lower left")
ax1.set_xscale('log')
ax1.grid()

#2nd plot 
p21=ax2.plot( X[::4],uPhi[::4]/ut[::4],'-', label = r"Angular velocity $\Omega$")      #angular velocity
ax2.set_ylim([0,0.03])


ax1.set_xlim([1e-1,100.])
ax2.set_xlim([1e-1,100.])
ax1.set_ylabel(r"Contribution to $\partial_tS_{r}$")
ax2.set(xlabel='r [M]')
ax3 = ax2.twinx()
ax3.set_ylabel('Density')
ax3.set_xscale('log')


p22=ax3.plot(X[::4],rh[::4]/2.*np.pi,'-.',label=r"Density $\rho$",color='red')
ax3.set_ylim(0, 2.5)
ax2.set_ylabel('Angular velocity')
ax2.grid()
ax2.set_xscale('log')

ax2.legend(handles = p21  + p22, loc="upper right")

fig1.savefig("Movie/pic-%04d.png"%kl)


####plot with avgs

fig2, (ax4, ax5) = plt.subplots(2,1,figsize=(9,12))

#1st plot 
ax4.plot(X[::4],PT[::4]/v4[::4],'-+',label="Thermal pressure")              #thermal pressure 
ax4.plot(X[::4],PD[::4]/v4[::4],label="Dynamic pressure")               #Dynamic pressure
ax4.plot(X[::4],PM[::4]/v4[::4]+TM[::4]/v4[::4],'-*',label="Magnetic pressure")      #magnetic pressure
ax4.plot(X[::4],CTHH[::4]/v4[::4]+CTHM[::4]/v4[::4],'-x',label=r"Centrifugal $\theta$")      #centrifugal theta
ax4.plot(X[::4],CPHH[::4]/v4[::4]+CPHM[::4]/v4[::4],'-_',label=r"Centrifugal $\phi$")      #centrifugal phi
ax4.plot(X[::4],GR[::4]/v4[::4],'-.',label="Gravity")               #gravity
ax4.plot(X[::4],TOTAL[::4]/v4[::4],'--', label ="Total") #total
ax4.legend(loc="lower left")
ax4.grid()
ax4.set_xscale('log')

#2nd plot 
p21=ax5.plot( X[::4],uPhi[::4]/ut[::4],'-', label = r"Angular velocity $\Omega$")      #angular velocity
ax5.set_ylim([0,0.03])


ax4.set_xlim([1e-1,100])
ax5.set_xlim([1e-1,100])
ax4.set_ylabel(r"Contribution to $\partial_tS_{r}$")
ax5.set(xlabel='r [M]')
ax5.set_xscale('log')


ax6 = ax5.twinx()
ax6.set_ylabel('Density')
ax6.set_xscale('log')

p22=ax6.plot(X[::4],rh[::4],'-.',label=r"Density $\rho$",color='red')
ax6.set_ylim(0, 2.5)
ax5.set_ylabel('Angular velocity')
ax5.grid()
ax5.legend(handles = p21  + p22, loc="upper right")

fig2.savefig("Movie/pic-avg-%04d.png"%kl)
