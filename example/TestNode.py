#!/usr/bin/env python
import numpy as np
import rbf.nodegen 
import matplotlib.pyplot as plt
import rbf.integrate

vert = np.array([[0.0,0.0],
                 [1.0,0.0],
                 [1.0,2.0],                 
                 [0.0,1.0]])
smp = np.array([[0,1],[1,2],[2,3],[3,0]])

@rbf.integrate.density_normalizer(vert,smp,10000)
def rho(p):
  return 1.0/(1.0 + 100*np.linalg.norm(p- np.array([0.4,0.5]),axis=1)**2)

vert_f = np.array([[0.5,0.25],[0.4,0.5],[0.5,0.75]])
smp_f = np.array([[0,1],[1,2]])

nodes_f,smpid_f = rbf.nodegen.surface(rho,vert_f,smp_f)

nodes,smpid = rbf.nodegen.volume(rho,vert,smp,fix_nodes=nodes_f)
print(smpid)
print(smpid_f)
plt.plot(nodes[smpid<0,0],nodes[smpid<0,1],'k.')
plt.plot(nodes[smpid>=0,0],nodes[smpid>=0,1],'ko')
plt.plot(nodes_f[smpid_f<0,0],nodes_f[smpid_f<0,1],'b.')
plt.plot(nodes_f[smpid_f>=0,0],nodes_f[smpid_f>=0,1],'bo')


plt.show()

