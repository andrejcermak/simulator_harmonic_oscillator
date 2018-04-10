from Tkinter import *
import time

class GraphPlot:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height=1000, bd=0)
        self.canvas.pack()
        self.point = self.canvas.create_oval(20, 195, 30, 205, fill="black")

    def simulate(self):
        posx = 0.1
        xspeed = 0.1
        i = 0
        m = 1
        u = -20
        k = 0.3
        g = 9.81
        rho = 1
        S = 5
        C = 0.4
        d_t = 0.004
        t = 0
        v = 0
        Fg = m * g
        F = k * u
        a = F / m
        max_u = 0
        for i in range(0, 30000):
            u2 = u
            v = v + a * d_t
            u = u - v * d_t
            F = k * u
            a = F / m
            t = t + d_t
            self.canvas.move(self.point, 10 * d_t, 10 * (u - u2))
            pos = self.canvas.coords(self.point)
            b = self.canvas.create_oval(pos[0] + 9, pos[1] + 9, pos[2], pos[3], fill="red")
            self.root.update()
            time.sleep(0.0001)

        self.root.mainloop()
