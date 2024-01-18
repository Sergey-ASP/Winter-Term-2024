import discretisedfield as df
import mag2exp
import magna.utils as mu
import matplotlib.pyplot as mpl
import xarray_extras.csv as xe
import pandas as pd
import numpy as np

filename = "MNP_Data/test/mnp_0/m_field_mnp_0.ovf"




read_field = df.Field.from_file(filename)

xarr = read_field.to_xarray()

nparr = np.array(xarr) 
print(xarr)
df = xarr.to_dataframe();

read_field.norm.sel('z').mpl()
# obj = mu.load_mnp(4, 'test')


# plotter = mu.MNP_Analyzer(obj)

# mu.MNP_Analyzer.k3d_center_vectors(plotter)



# cross_section = mag2exp.sans.cross_section(
#     read_field, method="unpol", polarisation=(0, 0, 1)
# )

# cross_section.sel(k_z=3).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
# )

# pp = mag2exp.sans.cross_section(
#     read_field, method="pp", polarisation=(0, 0, 1)
# )

# pm = mag2exp.sans.cross_section(
#     read_field, method="pn", polarisation=(0, 0, 1)
# )

# mp = mag2exp.sans.cross_section(
#     read_field, method="np", polarisation=(0, 0, 1)
# )

# min = mag2exp.sans.cross_section(
#     read_field, method="nn", polarisation=(0, 0, 1)
# )

# pp.sel(k_z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
# )

# pm.sel(k_z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
# )

# mp.sel(k_z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
# )

# min.sel(k_z=0).mpl.scalar(
#     cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
# )


mpl.show()