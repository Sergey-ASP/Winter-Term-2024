import micromagneticmodel as mm  # mm is just a shorter name we want to use later
import discretisedfield as df  # df is just a shorter name we want to use later
import matplotlib.pyplot as plt
import k3d as k3d
import magna.utils as mu

#  use r_tuple to specify radius of spheres
magna = mu.MNP(id=-1, name="test", n_layers=1, layer_radius=1, discretizations=(15,15,15), r_tuple=(24e-9, 3e-9, 3e-9), layer_dims=(1,2), shape='rectangle', axes_type='random_plane') #disc was set to all 10 initially
# magna.save_fields();
mu.quick_drive(magna)
M, A, K, U = magna.maku()

M.sel('z').mpl();
M.sel('x').mpl();
# plt.show();

M.to_file("magnaTestData_R_24e-9ORIGINAL.omf", representation="txt")



print("done")