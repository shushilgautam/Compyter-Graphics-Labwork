import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

window_width = 800
window_height = 600

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def draw_polygon(vertices):
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def key_callback(window, key, scancode, action, mods):
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

def main():
    if not glfw.init():
        return

    window = glfw.create_window(window_width, window_height, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    init()

    draw_polygon([(500, 100), (700, 100), (700, 300), (600, 400),(500,300)])


    glfw.terminate()

if __name__ == "__main__":
    main()

