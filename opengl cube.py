import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

window_width = 800
window_height = 600

# Vertices of the cube (changed to integer values)
cube_vertices = np.array([
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],  # Front face
    [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1],  # Back face
    [-1, 1, -1], [-1, 1, 1], [1, 1, 1], [1, 1, -1],  # Top face
    [-1, -1, -1], [1, -1, -1], [1, -1, 1], [-1, -1, 1],  # Bottom face
    [1, -1, -1], [1, 1, -1], [1, 1, 1], [1, -1, 1],  # Right face
    [-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [-1, 1, -1]  # Left face
], dtype=np.int32)

cube_indices = np.array([
    0, 1, 2, 3,  4, 5, 6, 7,  8, 9, 10, 11,  12, 13, 14, 15,  16, 17, 18, 19,  20, 21, 22, 23
], dtype=np.uint32)

window_vertices = np.array([
    [-0.5, -0.5, 0.0], [0.5, -0.5, 0.0], [0.5, 0.5, 0.0], [-0.5, 0.5, 0.0]
], dtype=np.float32)

window_indices = np.array([0, 1, 2, 3], dtype=np.uint32)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def draw_vertices(vertices, indices, color):
    glLineWidth(5.0)
    glColor3fv(color)
    glBegin(GL_QUADS)
    for i in range(0, len(indices), 4):
        for j in range(4):
            glVertex3iv(vertices[indices[i + j]])  # Using glVertex3iv for integer vertices
    glEnd()

def draw_cube_border(vertices, indices, color):
    glColor3fv(color)
    glBegin(GL_LINES)
    for i in range(0, len(indices), 4):
        for j in range(4):
            glVertex3iv(vertices[indices[i + j]])  # Using glVertex3iv for integer vertices
            glVertex3iv(vertices[indices[i + (j + 1) % 4]])  # Draw lines between consecutive vertices
    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(window_width, window_height, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, window_width / window_height, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

        draw_vertices(cube_vertices, cube_indices, [1.0, 0.0, 0.0])
        draw_cube_border(cube_vertices, cube_indices, [0.0, 0.0, 0.0])  # Draw black border for cube

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
