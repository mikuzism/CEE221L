# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import os 
os.chdir(r'C:\Users\mpmik')
from pyautocad import Autocad, APoint 
import array 

  #%%
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python")
print(acad.doc.Name)

#%%
# pattern 1
omega = 2*np.pi
v_n = 10
end_ang = 12*np.pi
unit_ang = np.pi/100
theta = np.linspace(0,end_ang,np.round(end_ang/unit_ang).astype(int))
x = v_n*theta/omega*np_cos(theta)
y = v_n*theta/
z = 0.1*np.arange(len(x))

n_points = len(x)
points_2d = np.array([x,y,z]).T.flatten()
points_double = array.array("d",points_2d)
acad.model.Add3dploy(points_double)

#%%
dp = pa.Apoint(0,0.5,0)
for i range(n_points):
    p1 =Apoint(x[i], y[i], z[i])
    if (i%5) == 0:
        text = acad.model.Addtext('Point %d' %i, p1+dp, 0.2)
        acad.model.AddCircle(p1, 0.01)
        
#%%
for obj in acad.iter_objects(['Circle','line']):
    print(obj.Objectname)
    