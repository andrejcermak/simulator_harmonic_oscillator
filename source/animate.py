from Tkinter import *
import time

class Animation:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=1000, height=1000, bd=0)
        self.canvas.pack()
        self.object = self.canvas.create_rectangle(450, 255,460, 265,  fill="black")
        self.line = self.canvas.create_line(250,255,650,255, fill="red")
        self.line1 = self.canvas.create_line(250,545,650,545, fill="red")
        self.line2 = self.canvas.create_line(250,400,650,400, fill="black")

    def animate_harmonic(self):
        posx=0.1
        xspeed=0.1
        i=0
        m=1
        u=-20
        k=0.3
        g=9.81
        rho=1
        S=5
        C=0.4
        d_t=0.001
        t=0
        v=0
        Fg=m*g
        F=k*u
        a=F/m
        max_u=0
        for i in range (0,1000000):
            u2=u
            if u2>max_u:
                max_u=u2
                print(pos[3])
            v=v+a*d_t
            u=u-v*d_t
            F=k*u
            a=F/m
            t=t+d_t
            self.canvas.move(self.object, 0, 7*(u-u2))
            pos=self.canvas.coords(self.object)
            #b=canvas.create_oval(pos[0]+9, pos[1]+9, pos[2], pos[3], fill="red")
            self.root.update()
            time.sleep(0.0001)

        root.mainloop()


    def animate_non_harmonic(self):
        posx = 0.1
        xspeed = 0.1
        i = 0
        m = 1
        u = -20
        k = 0.03
        g = 9.81
        rho = 0.01
        S = 5
        C = 0.4
        d_t = 0.01
        t = 0
        v = 0
        Fg = m * g
        F = k * u
        Fo = rho * S * v * v * C / 2
        a = F / m
        max_u = 0
        pos = self.canvas.coords(self.object)
        for i in range(0, 1000000):
            u2 = u
            if u2 > max_u:
                max_u = u2
                print(pos[3])
            v = v + a * d_t
            u = u - v * d_t
            F = k * u
            if (v < 0):
                F = (F + Fo);
            else:
                F = F - Fo;
            Fo = rho * S * v * v * C / 2;
            a = F / m
            t = t + d_t

            self.canvas.move(self.object, 0, 7 * (u - u2))
            self.root.update()
            time.sleep(0.0000001)