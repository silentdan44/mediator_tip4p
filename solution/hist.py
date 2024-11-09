import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
from MDAnalysis.analysis import distances

u = mda.Universe('npt.trr')
#u = mda.Universe('nvt.gro', 'npt.xtc') 
# Selecting atoms
atom1 = u.select_atoms('index 26')  # Atom 27 (Python uses zero-based indexing)
atom2 = u.select_atoms('index 85')  # Atom 86 N...N distance
atom3 = u.select_atoms('index 23')  # Atom 24 Si...Si distance
atom4 = u.select_atoms('index 82')  # Atom 83

distances_1_2 = []
distances_3_4 = []

for ts in u.trajectory:
    # Calculate distances for each frame
    d12 = distances.distance_array(atom1.positions, atom2.positions, box=u.dimensions)
    d34 = distances.distance_array(atom3.positions, atom4.positions, box=u.dimensions)

    # Store the first distance (since we are comparing single pairs)
    distances_1_2.append(d12[0][0])  
    distances_3_4.append(d34[0][0])  

distances_1_2 = np.array(distances_1_2)
distances_3_4 = np.array(distances_3_4)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(distances_1_2, bins=30, color='blue', alpha=0.7)
plt.title('N...N Distance Distribution')
plt.xlabel('Distance (Å)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(distances_3_4, bins=30, color='green', alpha=0.7)
plt.title('Si...Si Distance Distribution')
plt.xlabel('Distance (Å)')
plt.ylabel('Frequency')
plt.savefig("plot.png")
