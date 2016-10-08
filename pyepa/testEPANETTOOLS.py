from epanettools import epanet2 as et
import matplotlib.pyplot as plt

file_directory =  r"C:\0 Amin\QNRF\Git\experiments\resources\CTOWN.inp"

ret = et.ENopen(file_directory,"CTOWN.rpt","")
pres = []
nodes = []
time = []
et.ENopenH()
et.ENinitH(0)
while True:
    ret, t = et.ENrunH()
    ret, p = et.ENgetnodevalue(10, et.EN_PRESSURE)
    print t, p
    ret, t_step = et.ENnextH()
    if t % 3600 == 0:
        time.append(t/3600)
        pres.append(p)
    if t_step <= 0:
        break

et.ENcloseH()
print len(time), len(pres)
plt.plot(time, pres)
plt.grid()
plt.xlabel('Time (hr)')
plt.ylabel('Pressure (psi)')
plt.show()
