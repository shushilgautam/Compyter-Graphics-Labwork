import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from math import sin ,cos, radians
from copy import deepcopy
def rotate_xaxis(angle,ax1,vertices):
    # for x axis rotation
    angle=radians(angle)
    for i in range(len(vertices)):
        vertices[i][0]=vertices[i][0]
        y=vertices[i][1]
        vertices[i][1]=(y*cos(angle))-(vertices[i][2]*sin(angle))
        vertices[i][2]=(y*sin(angle))+(vertices[i][2]*cos(angle))
    plot_object(vertices,ax1,'green',"Rotation about X axis")
def rotate_yaxis(angle,ax2,vertices):
    # for x axis rotation
    angle=radians(angle)
    for i in range(len(vertices)):
        x=vertices[i][0]
        vertices[i][0]=(x*cos(angle))+(vertices[i][2]*sin(angle))
        vertices[i][1]=vertices[i][1]
        vertices[i][2]=(vertices[i][2]*cos(angle))+(x*sin(angle))
    plot_object(vertices,ax2,'red',"Rotation about y axis")
def rotate_zaxis(angle,ax3,vertices):
    # for x axis rotation
    angle=radians(angle)
    for i in range(len(vertices)):
        x=vertices[i][0]
        vertices[i][0]=(x*cos(angle))-(vertices[i][1]*sin(angle))
        vertices[i][1]=(x*sin(angle))+(vertices[i][1]*cos(angle))
        vertices[i][2]=vertices[i][2]
    plot_object(vertices,ax3,'orange',"Rotation about z axis")
# Function to plot a cube
def plot_object(vertices,ax,color,title):
    # Define the six faces of the cube using the vertices
    cube_size=7
    print(vertices)
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[0], vertices[3], vertices[7], vertices[4]]
    ]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='k', alpha=.25,label=title))  
    # Set axis labels
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    ax.set_xlim([-5, cube_size])
    ax.set_ylim([-5, cube_size])
    ax.set_zlim([-5, cube_size])
    ax.legend()
# Create a 3D plot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(2,2,1, projection='3d')
ax1=fig.add_subplot(2,2,2, projection='3d')
ax2=fig.add_subplot(2,2,3, projection='3d')
ax3=fig.add_subplot(2,2,4, projection='3d')
# Set the center and size of the cube


# Define the eight vertices of the cube
# if you want to change the value [x,y,z] the first four and last four has same z 
# ie 6,4 and first four x,y coordinates are same as last four x,y coordinates 
vertices = [
        [-1, 4, 4],
        [5, 4, 4],
        [5, 0, 4],
        [-1, 0, 4],
        [-1, 4, 2],
        [5, 4, 2],
        [5, 0, 2],
        [-1, 0, 2]
    ]
# Plot the cube
plot_object(vertices,ax,'blue',"Before Rotation")
angle=int(input("Enter the angle in degree :"))
rotate_xaxis(angle,ax1,deepcopy(vertices))
rotate_yaxis(angle,ax2,deepcopy(vertices))
rotate_zaxis(angle,ax3,deepcopy(vertices))
# Set plot limits

plt.suptitle("3D Rotation")
# Show the plot
plt.show()
