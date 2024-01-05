import discretisedfield as df
import micromagneticmodel as mm
import oommfc as mc
import matplotlib.pyplot as mpl;

system = mm.System(name='thetaevolve', T=60) # set temp as 60 K

mesh = df.Mesh(p1=(0,0,0), p2=(1e-7,1e-7,1e-9), cell=(1e-9,1e-9,1e-9))
system.m = df.Field(mesh, dim=3, value=(1,0,0), norm=1700e3)
system.m.plane('z').mpl()

system.dynamics = mm.Damping(alpha=0.1) + mm.Precession(gamma0=mm.consts.gamma0)
system.dynamics

evolver = mc.UHH_ThetaEvolver(fixed_timestep=2e-13)
td = mc.TimeDriver(evolver=evolver)
td.drive(system, t=5e-10, n=50)

system.m.plane('z').mpl()

mpl.show()

