import discretisedfield as df
import micromagneticmodel as mm
import numpy as np
import oommfc as oc
import ubermagutil.units as uu
import matplotlib.pyplot as mpl

np.random.seed(1)

region = df.Region(p1=(-160e-9, -160e-9, 0), p2=(160e-9, 160e-9, 20e-9))
mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 5e-9), bc="xyz")

system = mm.System(name="Box2")

system.energy = (
    mm.Exchange(A=1.6e-11) + mm.DMI(D=4e-3, crystalclass="T") + mm.Zeeman(H=(0, 0, 2e5))
)

Ms = 1.1e6


def m_fun(pos):
    return 2 * np.random.rand(3) - 1


# create system with above geometry and initial magnetisation
system.m = df.Field(mesh, nvdim=3, value=m_fun, norm=Ms)
system.m.sel("z").mpl()

# minimize the energy
md = oc.MinDriver()
md.drive(system)

system.m.to_file('testDataOriginal.vtk', representation="txt")

# Plot relaxed configuration: vectors in z-plane
system.m.sel("z").mpl()

# import mag2exp
# cross_section = mag2exp.sans.cross_section(
#     system.m, method="unpol", polarisation=(0, 0, 1)
# )

# cross_section.plane(z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
# )

# pp = mag2exp.sans.cross_section(
#     system.m, method="pp", polarisation=(0, 0, 1)
# )

# pm = mag2exp.sans.cross_section(
#     system.m, method="pn", polarisation=(0, 0, 1)
# )

# mp = mag2exp.sans.cross_section(
#     system.m, method="np", polarisation=(0, 0, 1)
# )

# min = mag2exp.sans.cross_section(
#     system.m, method="nn", polarisation=(0, 0, 1)
# )

# pp.plane(z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
# )

# pm.plane(z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
# )

# mp.plane(z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
# )

# min.plane(z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity"
# )
mpl.show()