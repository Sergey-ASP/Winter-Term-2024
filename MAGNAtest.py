import micromagneticmodel as mm  # mm is just a shorter name we want to use later
import discretisedfield as df  # df is just a shorter name we want to use later
import matplotlib.pyplot as plt
import k3d as k3d
import magna.utils as mu

magna = mu.MNP(id=-1, name="test", n_layers=1)
magna.save_fields();
magna.maku()

mu.quick_drive(magna)


print("done")