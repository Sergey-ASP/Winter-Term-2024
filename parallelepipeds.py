# DIMENSIONS 6.5nm long, 19 nm wide, and 49 nm high

import numpy as np
import math
from scipy.special import jv, gamma
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def fourier(mag, Q): # F.T. of sphere radius 0.5
    return mag*((4*math.pi/3.0)*gamma(5/2.0) * jv(3/2.0, Q/2.0)/np.float_power(Q/4.0, 3/2.0)/8.0)

def cross_section(Qx, Qy, n, m): # the result for the ++ cross-section
    theta = math.atan2(Qy, Qx)
    Q = math.sqrt(math.pow(Qx, 2) + math.pow(Qy, 2))
    term = np.square(np.abs(fourier(n, Q)))
    term += np.square(np.abs(fourier(m, Q)))*math.pow(math.sin(theta), 4)
    term += -(fourier(n, Q)*fourier(m, Q).conjugate() + \
              fourier(m, Q)*fourier(n, Q).conjugate()   ) * math.pow(math.sin(theta), 2)
    # the factor of 1E8 is to correspond with Sasview's intensity units
    return term*1E8/(4*math.pi*math.pow(0.5,3)/3.0)

WIDTH = 500
R = 2500

x = np.linspace(-5, 5, WIDTH)
y = np.linspace(-5, 5, WIDTH)
xs, ys = np.meshgrid(x, y)

vals = np.zeros_like(xs)
for i in range(WIDTH):
    for j in range(WIDTH):
        vals[i, j] = cross_section(xs[i, j], ys[i, j], n=math.sqrt(R), m=1)

fig = plt.figure()
contour_data = plt.contourf(xs, ys, vals, levels=MaxNLocator(nbins=20).tick_values(vals.min(), vals.max()))
plt.gca().set_aspect('equal')
cbar = fig.colorbar(contour_data)
plt.title("Magnetic sphere: R=" + str(R))
plt.xlabel("$Q_x / Å^{-2}$")
plt.ylabel("$Q_y / Å^{-2}$")
plt.show()

from ngsolve import *
from ngsolve.comp import *
from ngsolve.solve import *
from ngsolve.utils import *
from netgen.csg import *
import netgen.gui
from netgen.meshing import MeshingParameters

box = OrthoBrick(Pnt(-1,-1,-1),Pnt(1,1,1)).bc("outer")
magnet = Sphere(Pnt(0.5,0.25,0.5),0.5)
air = box - magnet
geo = CSGeometry()
geo.Add (air.mat("air"), transparent=True)
geo.Add (magnet.mat("magnet").maxh(3), col=(0.3,0.3,0.1))
geo.Draw()
mesh = Mesh(geo.GenerateMesh(maxh=3, curvaturesafety=1))
mesh.Curve(3)
mesh.GetMaterials(), mesh.GetBoundaries()
mur = mesh.MaterialCF({"magnet" : 0.05}, default=0)
# alter the nuclear SLD here      ^

mag = mesh.MaterialCF({"magnet" : (1,0,0)}, default=(0,0,0))
Draw (mag, mesh, "M-field", draw_surf=False)
Draw (mur, mesh, "Nuclear", draw_surf=False)
# output as vtk
vtk = VTKOutput(ma=mesh,coefs=[mur,mag],names=["M-field","Nuclear"],filename="sphere_refined",subdivision=3,legacy=True)
vtk.Do()