
import glfw
from OpenGL.GL import *
import numpy as np


primitive_type = GL_POLYGON


def compute_vertices():
    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    return np.array([[np.cos(angle), np.sin(angle)] for angle in angles])


def render(window):
    global primitive_type
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    vertices = compute_vertices()
    
    glBegin(primitive_type)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()
    
    glfw.swap_buffers(window)


def handle_key(window, key, scancode, action, mods):
    global primitive_type
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            primitive_type = GL_POINTS
        elif key == glfw.KEY_2:
            primitive_type = GL_LINES
        elif key == glfw.KEY_3:
            primitive_type = GL_LINE_STRIP
        elif key == glfw.KEY_4:
            primitive_type = GL_LINE_LOOP
        elif key == glfw.KEY_5:
            primitive_type = GL_TRIANGLES
        elif key == glfw.KEY_6:
            primitive_type = GL_TRIANGLE_STRIP
        elif key == glfw.KEY_7:
            primitive_type = GL_TRIANGLE_FAN
        elif key == glfw.KEY_8:
            primitive_type = GL_QUADS
        elif key == glfw.KEY_9:
            primitive_type = GL_QUAD_STRIP
        elif key == glfw.KEY_0:
            primitive_type = GL_POLYGON


def main():

    if not glfw.init():
        return

    window = glfw.create_window(480, 480, "2022063490-2-1.py", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, handle_key)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        render(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
