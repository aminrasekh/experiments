"""
This workflow runs extended-period simulation of CTOWN network and plots pressure reads
   for junction J193
Dependencies: epanettools and matplot modules
"""

from epanettools import epanet2 as et
from  epanettools.epanettools import EPANetSimulation
import matplotlib.pyplot as plt
import os

dir = os.path.abspath('testEPANETTOOLS.py')
dir = '\\'.join(dir.split('\\')[0:-2])
file_directory = dir + '\\resources\\CTOWN.inp'

ret = et.ENopen(file_directory, "CTOWN.rpt", "")
es = EPANetSimulation(file_directory)
n = es.network.nodes

junction = 'J193'

pres = []
nodes = []
time = []

et.ENopenH()
et.ENinitH(0)
while True:
    ret, t = et.ENrunH()
    ret, p = et.ENgetnodevalue(n[junction].index, et.EN_PRESSURE)
    print t, p
    ret, t_step = et.ENnextH()
    if t % 3600 == 0:
        time.append(t/3600)
        pres.append(p)
    if t_step <= 0:
        break

et.ENcloseH()

plt.plot(time, pres)
plt.grid()
plt.xlabel('Time (hr)')
plt.ylabel('Pressure (psi)')
plt.show()
