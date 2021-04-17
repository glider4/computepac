# 3-ODE Dynamical System Adams-Bashforth-Moulton estimation using
# Runge-Kutta four for initial values.
#
# 3D plotting using matplotlib Axes3D
#
# Input ODE equations as f1, f2, and f3
# Input t, x, y, z initial conditions
# Input a, b, n as lower bound, upper bound, num iterations
#
# Can run plot(a, b, n) to see results.  Can also run
# rk() or adams() by themselves, they output a list of lists
# result = [[xvals], [yvals], [zvals]] for plotting or analysis
#
# Note line in plot() that specifies RK vs. ABM results.  You can
# 3D plot RK results too if you want!
#
# ABM needs lots of iterations!  Do not run on <1000.
#
# To estimate a dynamical system of 3 ODEs (see examples folder):
#
# Note use of x, y, z as variables
#
#        def f1(x, y, z):
#            return (-1)*y - z
#
#        def f2(x, y, z):
#            return x + (0.1)*y
#
#        def f3(x, y, z):
#            return 0.1 + z*(x - 14)
#
#        res = ABM(f1, f2, f3, 0, 15, 15, 36, 0, 100, 10000)
#        res.plot()
#
# Output will be 3D matplotlib plot if you do this.  Other methods like res.adams() will
# show numerical results.
#

import numpy as np
import matplotlib.pyplot as plt


class ABM:
    def __init__(self, f1, f2, f3, t0: float, x0: float, y0: float, z0: float, a: float, b: float, n: int):
        # function 1, func2, func3, initial t0, x0, y0, z0, lower bound, upper, num iterations
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.t0 = t0
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.a = a
        self.b = b
        self.n = n

    def abm_comp(self):
        self.adams()

    # derivative functions
    def x1p(self, x1: float, x2: float, x3: float) -> float:
        return self.f1(x1, x2, x3)

    def x2p(self, x1: float, x2: float, x3: float) -> float:
        return self.f2(x1, x2, x3)

    def x3p(self, x1: float, x2: float, x3: float) -> float:
        return self.f3(x1, x2, x3)

    def adams(self) -> list:  # A-B-M computation, using RK4 to start
        a = self.a
        b = self.b
        n = self.n

        h = (b - a) / n
        y1 = np.zeros(n)  # initialize y1, y2, y3 matrices (and y_predictors)
        y2 = np.zeros(n)
        y3 = np.zeros(n)

        y_pred1 = np.zeros(n)
        y_pred2 = np.zeros(n)
        y_pred3 = np.zeros(n)

        for E in (0, 1, 2, 3):
            y1[E] = self.rk(E, 1)  # initial estimations to start A-B-M
            y2[E] = self.rk(E, 2)
            y3[E] = self.rk(E, 3)

        for i in range(
            4, n
        ):  # Equations change slightly, hard to refactor to make clean

            # x1p
            y_pred1[i] = y1[i - 1] + (
                h
                / 24
                * (
                    55 * self.x1p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 59 * self.x1p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + 37 * self.x1p(y1[i - 3], y2[i - 3], y3[i - 3])
                    - 9 * 0
                )
            )

            # x1p
            y1[i] = y1[i - 1] + (
                h
                / 24
                * (
                    9 * self.x1p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1])
                    + 19 * self.x1p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 5 * self.x1p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + self.x1p(y1[i - 3], y2[i - 3], y3[i - 3])
                )
            )

            # x2p
            y_pred2[i] = y2[i - 1] + (
                h
                / 24
                * (
                    55 * self.x2p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 59 * self.x2p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + 37 * self.x2p(y1[i - 3], y2[i - 3], y3[i - 3])
                    - 9 * (15 * (-8) - 15)
                )
            )

            # x2p
            y2[i] = y2[i - 1] + (
                h
                / 24
                * (
                    9 * self.x2p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1])
                    + 19 * self.x2p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 5 * self.x2p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + self.x2p(y1[i - 3], y2[i - 3], y3[i - 3])
                )
            )

            # x3p
            y_pred3[i] = y3[i - 1] + (
                h
                / 24
                * (
                    55 * self.x3p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 59 * self.x3p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + 37 * self.x3p(y1[i - 3], y2[i - 3], y3[i - 3])
                    - 9 * ((15 * 15) - ((8 / 3) * 36))
                )
            )

            # x3p
            y3[i] = y3[i - 1] + (
                h
                / 24
                * (
                    9 * self.x3p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1])
                    + 19 * self.x3p(y1[i - 1], y2[i - 1], y3[i - 1])
                    - 5 * self.x3p(y1[i - 2], y2[i - 2], y3[i - 2])
                    + self.x3p(y1[i - 3], y2[i - 3], y3[i - 3])
                )
            )

        return [y1, y2, y3]

    def rk(self, which_y: int = 9, which_x: int = 9) -> list:  # Runge-Kutta 4 computation by itself
        # which_y indicator for which Y1, Y2, Y3 val is needed to be return by function
        # which_x means x1, x2, x3 when calling for values Y1, Y2, Y3, etc...

        a = self.a
        b = self.b
        n = self.n

        h = (b - a) / n  # step size
        p = 0  # flag for while loop

        # initialize lists for plot
        t = np.zeros(int(n + 1))
        x1 = np.zeros(int(n + 1))
        x2 = np.zeros(int(n + 1))
        x3 = np.zeros(int(n + 1))

        # define initial values
        t[0] = self.t0
        x1[0] = self.x0
        x2[0] = self.y0
        x3[0] = self.z0

        # initialize slots for values of RK4
        i = np.zeros(4)  # for x1
        j = np.zeros(4)  # for x2
        k = np.zeros(4)  # for x3

        # iterate n times
        while p < n:
            i[0] = h * self.x1p(x1[p], x2[p], x3[p])
            j[0] = h * self.x2p(x1[p], x2[p], x3[p])
            k[0] = h * self.x3p(x1[p], x2[p], x3[p])

            i[1] = h * self.x1p(
                x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0]
            )
            j[1] = h * self.x2p(
                x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0]
            )
            k[1] = h * self.x3p(
                x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0]
            )

            i[2] = h * self.x1p(
                x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1]
            )
            j[2] = h * self.x2p(
                x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1]
            )
            k[2] = h * self.x3p(
                x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1]
            )

            i[3] = h * self.x1p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])
            j[3] = h * self.x2p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])
            k[3] = h * self.x3p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])

            x1[p + 1] = x1[p] + (1 / 6) * (i[0] + (2 * i[1]) + (2 * i[2]) + i[3])
            x2[p + 1] = x2[p] + (1 / 6) * (j[0] + (2 * j[1]) + (2 * j[2]) + j[3])
            x3[p + 1] = x3[p] + (1 / 6) * (k[0] + (2 * k[1]) + (2 * k[2]) + k[3])

            t[p + 1] = t[p] + h

            p += 1  # advance flag variable

        if which_y in (0, 1, 2, 3):
            if which_x == 1:
                return x1[which_y]
            elif which_x == 2:
                return x2[which_y]
            elif which_x == 3:
                return x3[which_y]
            else:
                return []

        return [x1, x2, x3]

    def plot3d(self):  # lower bound, upper bound, num iterations
        # res = rk(a, b, n)
        res = self.adams()

        # Plotting
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        ax.plot(res[0], res[1], res[2], linewidth=1.0, color="darkblue")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.title("Adams-Bashforth-Moulton Estimation")
        plt.style.use("ggplot")
        plt.show()
