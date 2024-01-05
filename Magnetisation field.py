import discretisedfield as df  # df is just a shorter name
import matplotlib.pyplot as mpl

p1 = (0, -20e-9, 0)  # point 1
p2 = (100e-9, 20e-9, 10e-9)  # point 2

region = df.Region(p1=p1, p2=p2)

region.pmin  # minimum coordinate in the region
region.pmax  # maximum coordinate in the region
region.centre  # the region centre
region.edges  # edge lengths of the region

## region.mpl()

cell = (10e-9, 10e-9, 10e-9)  # discretisation cell
mesh = df.Mesh(region=region, cell=cell)  # mesh definition
mesh.n  # number of discretisation cells
len(mesh)  # total number of discretisation cells

# mesh.mpl()

# creating magnetic field that is spacially dependent
def m_value(point):
    x, y, z = point  # unpack position into individual components
    if y > 0:
        return (1, 0, 0)
    else:
        return (-1, 1, 0)

m = df.Field(mesh, dim=3, value=m_value)

# m.plane('z').mpl()


#     DISK

t = 10e-9  # thickness (m)
d = 120e-9  # diameter (m)
cell = (5e-9, 5e-9, 5e-9)  # discretisation cell size (m)
Ms = 1e7  # saturation magnetisation (A/m)

region = df.Region(p1=(-d/2, -d/2, -t/2), p2=(d/2, d/2, t/2))
mesh = df.Mesh(region=region, cell=cell)

def Ms_value(point):
    x, y, z = point
    if (x**2 + y**2)**0.5 < d/2:
        return Ms
    else:
        return 0

m = df.Field(mesh, dim=3, value=(1, 0, 0), norm=Ms_value)

# m.norm.plane('z').mpl()

def m_value(pos):
    x, y, z = pos
    if y <= 0:
        return (-1, 0, 0)
    else:
        return (1, 1, 1)

m = df.Field(mesh, dim=3, value=m_value, norm=Ms_value)

# m.plane('z').mpl()

# EXCERCISE

t = 10e-9  # thickness (m)
cell = (5e-9, 5e-9, 5e-9)  # discretisation cell size (m)
p1 = (0, 0, 0)
p2 = (100e-9, 50e-9, t)
region = df.Region(p1, p2)
mesh = df.Mesh(region=region, cell=cell)
Ms = 8e6

def Ms_value(point):
    x,y,z = point
    if x<50e-9 and y> 35e-9:
        return 0
    else:
        return Ms

def m_value(pos):
    x,y,z = pos
    if x>=20e-9 and x<=30e-9:
        return (1,1,-1)
    else:
        return (1,1,1)

m = df.Field(mesh, 3, m_value, Ms_value)
m.plane('z').mpl()


mpl.show();