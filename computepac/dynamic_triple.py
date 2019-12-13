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
#        abm_comp(f1, f2, f3, 0, 15, 15, 36, 0, 100, 10000)
#        plot(0, 100, 10000)
#
# You can un-comment the "plot" function call in abm_comp if you want it
# to auto-plot the results
#
# Output will be 3D matplotlib plot if you do this
#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def abm_comp(f1, f2, f3, t0, x0, y0, z0, a, b, n):
    # function 1, func2, func3, initial t0, x0, y0, z0, lower bound, upper, num iterations

    global params
    params = [t0, x0, y0, z0]

    # plot(a, b, n)


# derivative functions
def x1p(x1, x2, x3):
    return f1(x1, x2, x3)


def x2p(x1, x2, x3):
    return f2(x1, x2, x3)


def x3p(x1, x2, x3):
    return f3(x1, x2, x3)


def adams(a, b, n):  # A-B-M computation, using RK4 to start

    h = (b - a) / n
    y1 = np.zeros(n)  # initialize y1, y2, y3 matrices (and y_predictors)
    y2 = np.zeros(n)
    y3 = np.zeros(n)

    y_pred1 = np.zeros(n)
    y_pred2 = np.zeros(n)
    y_pred3 = np.zeros(n)

    for E in (0, 1, 2, 3):
        y1[E] = rk(a, b, n, E, 1)  # initial estimations to start A-B-M
        y2[E] = rk(a, b, n, E, 2)
        y3[E] = rk(a, b, n, E, 3)

    for i in range(4, n):  # Equations change slightly, hard to refactor to make clean

        # x1p
        y_pred1[i] = y1[i - 1] + (h / 24 * (55 *
                                            x1p(y1[i - 1], y2[i - 1], y3[i - 1]) - 59 *
                                            x1p(y1[i - 2], y2[i - 2], y3[i - 2]) + 37 *
                                            x1p(y1[i - 3], y2[i - 3], y3[i - 3]) - 9 * 0))

        # x1p
        y1[i] = y1[i - 1] + (h / 24 * (9 *
                                       x1p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1]) + 19 *
                                       x1p(y1[i - 1], y2[i - 1], y3[i - 1]) - 5 *
                                       x1p(y1[i - 2], y2[i - 2], y3[i - 2]) +
                                       x1p(y1[i - 3], y2[i - 3], y3[i - 3])))

        # x2p
        y_pred2[i] = y2[i - 1] + (h / 24 * (55 *
                                            x2p(y1[i - 1], y2[i - 1], y3[i - 1]) - 59 *
                                            x2p(y1[i - 2], y2[i - 2], y3[i - 2]) + 37 *
                                            x2p(y1[i - 3], y2[i - 3], y3[i - 3]) - 9 * (15 * (-8) - 15)))

        # x2p
        y2[i] = y2[i - 1] + (h / 24 * (9 *
                                       x2p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1]) + 19 *
                                       x2p(y1[i - 1], y2[i - 1], y3[i - 1]) - 5 *
                                       x2p(y1[i - 2], y2[i - 2], y3[i - 2]) +
                                       x2p(y1[i - 3], y2[i - 3], y3[i - 3])))

        # x3p
        y_pred3[i] = y3[i - 1] + (h / 24 * (55 *
                                            x3p(y1[i - 1], y2[i - 1], y3[i - 1]) - 59 *
                                            x3p(y1[i - 2], y2[i - 2], y3[i - 2]) + 37 *
                                            x3p(y1[i - 3], y2[i - 3], y3[i - 3]) - 9 * ((15 * 15) - ((8 / 3) * 36))))

        # x3p
        y3[i] = y3[i - 1] + (h / 24 * (9 *
                                       x3p(y_pred1[i - 1], y_pred2[i - 1], y_pred3[i - 1]) + 19 *
                                       x3p(y1[i - 1], y2[i - 1], y3[i - 1]) - 5 *
                                       x3p(y1[i - 2], y2[i - 2], y3[i - 2]) +
                                       x3p(y1[i - 3], y2[i - 3], y3[i - 3])))

    return [y1, y2, y3]


def rk(a, b, n, whichy=9, whichx=9):  # Runge-Kutta 4 computation by itself
    # a lower bound
    # b upper bound
    # n number of steps
    # whichy indicator for which Y1, Y2, Y3 val is needed to be return by function
    # whichx means x1, x2, x3 when calling for values Y1, Y2, Y3, etc...

    h = (b - a) / n  # step size
    p = 0  # flag for while loop

    # intialize lists for plot
    t = np.zeros(int(n + 1))
    x1 = np.zeros(int(n + 1))
    x2 = np.zeros(int(n + 1))
    x3 = np.zeros(int(n + 1))

    # define initial values
    t[0] = params[0]
    x1[0] = params[1]
    x2[0] = params[2]
    x3[0] = params[3]

    # initialize slots for values of RK4
    i = np.zeros(4)  # for x1
    j = np.zeros(4)  # for x2
    k = np.zeros(4)  # for x3

    # iterate n times
    while p < n:
        i[0] = h * x1p(x1[p], x2[p], x3[p])
        j[0] = h * x2p(x1[p], x2[p], x3[p])
        k[0] = h * x3p(x1[p], x2[p], x3[p])

        i[1] = h * x1p(x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0])
        j[1] = h * x2p(x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0])
        k[1] = h * x3p(x1[p] + (1 / 2) * i[0], x2[p] + (1 / 2) * j[0], x3[p] + (1 / 2) * k[0])

        i[2] = h * x1p(x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1])
        j[2] = h * x2p(x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1])
        k[2] = h * x3p(x1[p] + (1 / 2) * i[1], x2[p] + (1 / 2) * j[1], x3[p] + (1 / 2) * k[1])

        i[3] = h * x1p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])
        j[3] = h * x2p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])
        k[3] = h * x3p(x1[p] + i[2], x2[p] + j[2], x3[p] + k[2])

        x1[p + 1] = x1[p] + (1 / 6) * (i[0] + (2 * i[1]) + (2 * i[2]) + i[3])
        x2[p + 1] = x2[p] + (1 / 6) * (j[0] + (2 * j[1]) + (2 * j[2]) + j[3])
        x3[p + 1] = x3[p] + (1 / 6) * (k[0] + (2 * k[1]) + (2 * k[2]) + k[3])

        t[p + 1] = t[p] + h

        p += 1  # advance flag variable

    if whichy in (0, 1, 2, 3):
        if whichx == 1:
            return x1[whichy]
        elif whichx == 2:
            return x2[whichy]
        elif whichx == 3:
            return x3[whichy]
        else:
            return

    return [x1, x2, x3]


def plot(a, b, n):  # lower bound, upper bound, num iterations
    # res = rk(a, b, n)
    res = adams(a, b, n)

    # Plotting
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(res[0], res[1], res[2], linewidth=1.0, color="darkblue")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title("Adams-Bashforth-Moutlon Estimation")
    plt.style.use('ggplot')
    plt.show()
