import numpy as np
import matplotlib.pyplot as plt
import torch

side = 5
phi = 0.02
theta = 0.07
illumination = ".,-~:;=!*#$@"   

# initial coords
vertices = torch.tensor([[1, 1, 1], 
                        [1, -1, -1], 
                        [-1, 1, -1], 
                        [-1, -1, 1]], dtype=torch.float32)

# create faces from vertices
face = torch.tensor([[0, 1, 2], 
                    [0, 1, 3], 
                    [0, 2, 3], 
                    [1, 2, 3]], dtype=torch.int)

# rotation matrix x-axis
rotation_x = torch.tensor([[1, 0, 0],
                        [0, np.cos(theta), np.sin(theta)],
                        [0, -np.sin(theta), np.cos(theta)]], dtype=torch.float32)

# rotation matrix y-axis
rotation_y = torch.tensor([[np.cos(theta), 0, np.sin(theta)],
                        [0, 1, 0],
                        [-np.sin(theta), 0, np.cos(theta)]], dtype=torch.float32)

# rotation matrix z-axis
rotation_z = torch.tensor([[np.cos(theta), np.sin(theta), 0],
                        [-np.sin(theta), np.cos(theta), 0],
                        [0, 0, 1]], dtype=torch.float32)

# dot product of vertices and rotation matrix
def rotate(vertices, axis):
    return vertices @ axis.T

# normal of triangle in 3D space  
def normal():
    

    # face = vertices[face[0]]
    # normal is cross product of 2 vectors on a face
    pass

# light coming from (0, 1, -1)
illumination = ".,-~:;=!*#$@"

# surface normal is perperndicular to face
# since all faces will have same surface normal
# calc one and use for all
#(Nx, Ny, Nz) = 


#def project(vertices): d
result = vertices[face]
print(result)