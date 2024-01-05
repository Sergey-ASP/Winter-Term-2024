import micromagneticmodel as mm  # mm is just a shorter name we want to use later
import discretisedfield as df  # df is just a shorter name we want to use later
import matplotlib as mpl;
import k3d as k3d
import matplotlib.pyplot as plt
import oommfc as mc

## FIRST TUTORIAL

plot = k3d.Plot()

system = mm.System(name='first_ubermag_simulation')

A = 1e-12  # exchange energy constant (J/m)
H = (5e6, 0, 0)  # external magnetic field in the x-direction (A/m)
system.energy = mm.Exchange(A=A) + mm.Demag() + mm.Zeeman(H=H)

L = 50e-9  # cubic sample edge length (m)
region = df.Region(p1=(0, 0, 0), p2=(L, L, L))
mesh = df.Mesh(region=region, n=(10, 10, 10))

Ms = 8e6  # saturation magnetisation (A/m)
system.m = df.Field(mesh, dim=3, value=(0, 1, 0), norm=Ms)

md = mc.MinDriver()
md.drive(system)

    #USE plane() to get a graph along an axis, seems that sel() is depreciated
system.m.plane('z').mpl()

plt.show();