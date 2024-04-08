import glfw
from OpenGL.GL import *
import numpy as np


def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([1.,0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0.,0.]))
    glVertex2fv(np.array([0.,1.]))
    glEnd()
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv((T @ np.array([0, 0.5, 1]))[:-1])
    glVertex2fv((T @ np.array([0, 0., 1.]))[:-1])
    glVertex2fv((T @ np.array([0.5, 0., 1.]))[:-1])
    glEnd()


def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480, "2022063490-2-2", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        angle = glfw.get_time()
        
        
        R = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0., 0., 1.]
        ])

        T = np.array([
            [1., 0, 0.5],  
            [0, 1., 0], 
            [0, 0, 1.]
        ])


        M = R@T
        render(M)        
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
