import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of a regular tetrahedron
vertices = np.array([
    [1, 1, 1],
    [1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]
])

# Define the faces of the tetrahedron (each face is a triangle)
face = torch.tensor([[0, 1, 2],
                    [0, 1, 3],
                    [0, 2, 3],
                    [1, 2, 3]])

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each face of the tetrahedron
ax.add_collection3d(Poly3DCollection(vertices[faces], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Set the limits of the plot
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Label the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
