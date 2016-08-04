import numpy as np
import matplotlib.pyplot as plt


[bursttime_a,He_env_mass_a] = [1.0169e6,4.063e-2]  # NACRE
[bursttime_b,He_env_mass_b] = [1.0426e6,4.165e-2]  # HHR
[bursttime_c,He_env_mass_c] = [1.0161e6,4.061e-2]  # HYBRID NO DIP
[bursttime_d,He_env_mass_d] = [1.0431e6,4.175e-2]  # HYBRID DIP


plt.scatter(bursttime_a,He_env_mass_a,marker='o',s=80,facecolors='black') # NACRE
plt.scatter(bursttime_b,He_env_mass_b,marker='o',s=80,facecolors='dodgerblue') # HHR

#plt.scatter(bursttime_c,He_env_mass_c,marker='o',s=80,facecolors='red') # HYBRID NO DIP
plt.scatter(bursttime_d,He_env_mass_d,marker='o',s=80,facecolors='red') # HYBRID DIP


plt.xlabel('Time since previous burst [yrs]')
#plt.xscale('log')

plt.ylabel('$M_\mathrm{env}$ $[\mathrm{M}_\odot]$')
#plt.yscale('log')

#plt.legend(loc=4)
plt.xlim([1.01e6,1.05e6])
plt.ylim([4.05e-2,4.19e-2])

fig = plt.gcf()
fig.set_size_inches(10.00, 4.00)

plt.show()

