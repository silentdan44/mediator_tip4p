import plumed
import matplotlib.pyplot as plt
import numpy as np

data=plumed.read_as_pandas("./fes.dat")

nbins = -1

with open("fes.dat", 'r') as file:
    for line in file:
        if "nbins_d1" in line:
            nbins = int(line.split()[3])

assert nbins != -1

fig, ax = plt.subplots()
x1, y1 = data["d1"][:nbins], data["d2"][::nbins]

z = np.array(data["file.free"])
z = z.reshape(len(y1), len(x1))

CS = ax.contourf(x1, y1, z, levels=20)
#plt.xlim(-0.9, 0.9)
#plt.ylim(1.8, 2.7)
fig.colorbar(CS)
plt.savefig("1.png")
plt.show()
