import oommfc as mc
import discretisedfield as df
import micromagneticmodel as mm

region = df.Region(p1=(-50e-9, -50e-9, -50e-9), p2=(50e-9, 50e-9, 50e-9))
mesh = df.Mesh(region=region, cell=(5e-9, 5e-9, 5e-9))

system = mm.System(name='hysteresis')
system.energy = mm.Exchange(A=1e-12) + mm.UniaxialAnisotropy(K=4e5, u=(0, 0, 1)) + mm.DMI(D=1e-3, crystalclass='T')# + mm.Demag()

def Ms_fun(point):
    x, y, z = point
    if x**2 + y**2 + z**2 <= 50e-9**2:
        return 1e6
    else:
        return 0

system.m = df.Field(mesh, nvdim=3, value=(0, 0, -1), norm=Ms_fun, valid="norm")

Hmin = (0, 0, -1/mm.consts.mu0)
Hmax = (0, 0, 1/mm.consts.mu0)
n = 21 # number of steps

hd = mc.HysteresisDriver()
hd.drive(system, Hmin=Hmin, Hmax=Hmax, n=n)
system.m.plane('y').mpl()