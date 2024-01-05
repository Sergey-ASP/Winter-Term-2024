import oommfc as mc
import discretisedfield as df
import micromagneticmodel as mm

region = df.Region(p1=(0, 0, 0), p2=(10e-9, 10e-9, 10e-9))
mesh = df.Mesh(region=region, n=(10, 10, 10))
mesh.mpl()

system = mm.System(name='energy_computations')

A = 1e-11  # exchange energy constant (J/m)
H = (0.1/mm.consts.mu0, 0, 0)  # external magnetic field (A/m)
K = 1e3  # uniaxial anisotropy constant (J/m3)
u = (1, 1, 1)  # uniaxial anisotropy axis

system.energy = (mm.Exchange(A=A) +
                 mm.Demag() +
                 mm.Zeeman(H=H) +
                 mm.UniaxialAnisotropy(K=K, u=u))

system.energy

Ms = 8e5  # saturation magnetisation (A/m)

system.m = df.Field(mesh, dim=3, value=(0, 0, 1), norm=Ms)

Heff = mc.compute(system.energy.effective_field, system)
Heff.plane('x').mpl()

#  all computations are done using compute()