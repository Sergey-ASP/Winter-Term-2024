import discretisedfield as df
import mag2exp
import magna.utils as mu
import matplotlib.pyplot as mpl
import xarray_extras.csv as xe
import pandas as pd
import numpy as np

filename = "A_Raw_Example-1.omf"




read_field = df.Field.from_file(filename)
read_field.norm.sel('z').mpl()

cross_section = mag2exp.sans.cross_section(
    read_field, method="unpol", polarisation=(0, 0, 1)
)

cross_section.sel(k_z=0).mpl.scalar(
    # cmap="gray",
    colorbar_label=r"Intensity",
    colorbar=True,
    vmax=.0005,
    vmin=-.0005
    
)
    # norm=colors.LogNorm(vmin=1e-3, vmax=cross_section.real.array.max()),

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