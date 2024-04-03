
import glfw
from OpenGL.GL import *
import sys

# Window dimensions
window_width = 800
window_height = 600

# Initialize OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_width, 0.0, window_height, -1.0, 1.0)

# Function to draw a point with increased size
def draw_point(x, y):
    glPointSize(10.0)  # Increase point size to 10
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

# Function to draw a line
def draw_line(x1, y1, x2, y2):
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

# Function to draw a polygon
def draw_polygon(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

# Display function
def display(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)  # Set drawing color to black

    # Draw a point with increased size
    draw_point(200, 500)

    # Draw a line
    draw_line(200, 200, 500, 500)

    # Draw a polygon
    draw_polygon([(500, 100), (700, 100), (700, 300), (600, 400),(500,300)])

    glfw.swap_buffers(window)

# Keyboard callback function
def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

# Main function
def main():
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(window_width, window_height, "Point Line & Polygon", None, None)  # Change title here
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        display(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
    