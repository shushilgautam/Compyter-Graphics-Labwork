import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

window_width = 800
window_height = 600

points = []
line_width = 5.0  # Initial line width

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def draw_lines():
    glColor3f(0.0, 0.0, 1.0)  # Blue color for lines
    glLineWidth(line_width)  # Set line width
    glBegin(GL_LINES)
    for i in range(0, len(points), 2):
        glVertex2f(*points[i])
        if i + 1 < len(points):
            glVertex2f(*points[i + 1])
    glEnd()

def mouse_button_callback(window, button, action, mods):
    global points
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        xpos, ypos = glfw.get_cursor_pos(window)
        xpos = 2 * xpos / window_width - 1
        ypos = 1 - 2 * ypos / window_height
        points.append((xpos, ypos))
        if len(points) % 2 == 0:
            points.append((xpos, ypos))



def main():
    if not glfw.init():
        return

    window = glfw.create_window(window_width, window_height, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    

    init()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(-1, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        draw_lines()

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
