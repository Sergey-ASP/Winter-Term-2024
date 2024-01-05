
import discretisedfield as df  # df is just a shorter name
import matplotlib.pyplot as mpl
import numpy as np
import micromagneticmodel as mm
import oommfc as oc

t = 1e-9  # thickness (m)
d = 7e-9  # diameter (m)
cell = (.5e-9, .5e-9, .5e-9)  # discretisation cell size (m)
Ms = 1e7  # saturation magnetisation (A/m)

region = df.Region(p1=(-d/2 -d, -d/2 -d, -t/2), p2=(d/2+d, d/2+d, t/2))
mesh = df.Mesh(region=region, cell=cell)

def Ms_value(point):
    x, y, z = point
    if (x**2 + y**2)**0.5 < d/2 or (x**2 + (y-d)**2)**0.5 < d/2 or (x**2 + (y+d)**2)**0.5 < d/2 or ((x+d*(np.sqrt(3)/2))**2 + (y+d/2)**2)**0.5 < d/2 or ((x-d*(np.sqrt(3)/2))**2 + (y+d/2)**2)**0.5 < d/2 or ((x+d*(np.sqrt(3)/2))**2 + (y-d/2)**2)**0.5 < d/2 or ((x-d*(np.sqrt(3)/2))**2 + (y-d/2)**2)**0.5 < d/2:
        return Ms
    else:
        return 0

# m.norm.plane('z').mpl()
system = mm.System(name="sansTest")

system.energy = (
    mm.Exchange(A=1.6e-11) + mm.DMI(D=4e-3, crystalclass="T") + mm.Zeeman(H=(0, 0, 2e5))
)

def m_value(pos):
    return 2 * np.random.rand(3) -1

system.m = df.Field(mesh, dim=3, value=m_value, norm=Ms_value)

md = oc.MinDriver()
md.drive(system)
system.m.plane('z').mpl()

import mag2exp
cross_section = mag2exp.sans.cross_section(
    system.m, method="unpol", polarisation=(0, 0, 1)
)

cross_section.plane(z=0).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
)

import matplotlib.colors as colors

cross_section.plane(z=0).mpl.scalar(
    cmap="gray",
    colorbar_label=r"Intensity",
    norm=colors.LogNorm(vmin=1e-3, vmax=cross_section.real.array.max()),
)

mpl.show()