import micromagneticmodel as mm  # mm is just a shorter name we want to use later
import discretisedfield as df  # df is just a shorter name we want to use later
import matplotlib.pyplot as plt
import k3d as k3d
import magna.utils as mu

#  use r_tuple to specify radius of spheres
# magna = mu.MNP(id=-1, name="test", n_layers=1, layer_radius=3, discretizations=(15,15,15), r_tuple=(4e-9, 3e-9, 3e-9)) #, axes_type='random_plane') #disc was set to all 10 initially
# magna.save_fields();
magna = mu.MNP(id=-1)
mu.quick_drive(magna)
M, A, K, U = magna.maku()

M.sel('z').mpl();
M.sel('x').mpl();
M.sel('y').mpl();
plt.show();

# M.to_file("magnaTestData_d10_r30_l3.omf", representation="txt")



print("done")