import discretisedfield as df
import mag2exp
import magna.utils as mu
import matplotlib.pyplot as mpl
import xarray_extras.csv as xe
import pandas as pd
import numpy as np

filename = "testData.omf"




read_field = df.Field.from_file(filename)

# xarr = read_field.to_xarray()

# nparr = np.array(xarr) 
# print(xarr)
# df = xarr.to_dataframe();

read_field.norm.sel('z').mpl()
# obj = mu.load_mnp(4, 'test')



cross_section = mag2exp.sans.cross_section(
    read_field, method="unpol", polarisation=(1, 0, 0)
)

cross_section.sel(k_z=3).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", vmax=60
)

pp = mag2exp.sans.cross_section(
    read_field, method="pp", polarisation=(1, 0, 0)
)

pm = mag2exp.sans.cross_section(
    read_field, method="pn", polarisation=(1, 0, 0)
)

mp = mag2exp.sans.cross_section(
    read_field, method="np", polarisation=(1, 0, 0)
)

min = mag2exp.sans.cross_section(
    read_field, method="nn", polarisation=(1, 0, 0)
)

pp.sel(k_z=0).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", #vmax=60
)

pm.sel(k_z=0).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", #vmax=60
)

mp.sel(k_z=0).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", #vmax=60
)

min.sel(k_z=0).mpl.scalar(
    cmap="gray", interpolation="spline16", colorbar_label=r"Intensity", #vmax=60
)


mpl.show()