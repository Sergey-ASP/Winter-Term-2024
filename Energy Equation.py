import oommfc as oc
import discretisedfield as df
import micromagneticmodel as mm
import matplotlib.pyplot as plt

p1 = (0, 0, 0)
p2 = (10e-9, 1e-9, 1e-9)
cell = (1e-9, 1e-9, 1e-9)

region = df.Region(p1=p1, p2=p2)
mesh = df.Mesh(p1=p1, p2=p2, cell=cell)

# mesh.mpl()

system = mm.System(name='zeeman')  # create the (micromagnetic) system object

H = (0, 0, 1e6)  # external magnetic field (A/m)
Ms = 8e6  # saturation magnetisation (A/m)
system.energy = mm.Zeeman(H=H)  # define system's Hamiltonian
system.m = df.Field(mesh, dim=3, value=(1, 0, 1), norm=Ms)  # define initial magnetisation

# system.m.plane('y').mpl()

md = oc.MinDriver()  # create energy minimisation driver
md.drive(system)  # run energy minimisation

# system.m.plane('y').mpl()

system.energy.zeeman.H = (-1e6, 0, 0)
md.drive(system)
# system.m.plane('y').mpl()

# UNIAXIAL ANISOTROPY

system = mm.System(name='uniaxial_anisotropy')
system.energy = mm.UniaxialAnisotropy(K=6e6, u=(1, 0, 1))

def m_initial(pos):
    x, y, z = pos
    if x <= 5e-9:
        return (-1, 0, -0.1)
    else:
        return (1, 0, 0.1)

system.m = df.Field(mesh, dim=3, value=m_initial, norm=Ms)

# system.m.plane('y').mpl()

md.drive(system)
# system.m.plane('y').mpl()

# EXCHANGE ENERGY

system = mm.System(name='exchange')
system.energy = mm.Exchange(A=8e-12)

def m_initial(pos):
    x, y, z = pos
    if x <= 5e-9:
        return (0, 0, 1)
    else:
        return (1, 0, 0)

system.m = df.Field(mesh, dim=3, value=m_initial, norm=Ms)

# system.m.plane('y').mpl()

# Dzyaloshinskii-Moriya energy

system = mm.System(name='dmi')
system.energy = mm.DMI(crystalclass='Cnv_z', D=3e-3)
system.m = df.Field(mesh, dim=3, value=(0, 0, 1), norm=Ms)

md.drive(system)

# system.m.plane('y').mpl()

# EXCHANGE AND ZEEMAN ENERGIES

system = mm.System(name='exchange_and_zeeman')

# We can add multiple interactions using the 'plus' operator
system.energy = mm.Exchange(A=8e-12) + mm.Zeeman(H=(0, 0, -1e6))

def m_initial(pos):
    x, y, z = pos
    if x <= 5e-9:
        return (0, 0, 1)
    else:
        return (1, 0, 0)

system.m = df.Field(mesh, nvdim=3, value=m_initial, norm=Ms)

system.m.sel('y').mpl()

plt.show()