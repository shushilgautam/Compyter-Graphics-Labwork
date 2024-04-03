import glfw
from OpenGL.GL import *

# Window dimensions
window_width = 800
window_height = 600

# Initialize OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white

# Display function for window
def display_window():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

# Main function
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(window_width, window_height, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set up OpenGL
    init()

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Set up view and projection matrices
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1, 1, -1, 1, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Draw the window
        glColor3f(0.0, 0.0, 0.0)  # Set drawing color to black
        display_window()

        # Swap front and back buffers
        glfw.swap_buffers(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()