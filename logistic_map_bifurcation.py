import matplotlib.pyplot as plt

xnum = 500
xa = 2.
xb = 4.
iterations = 1000
startpop = 0.5

r_plot = []
y_plot = []

for i in range(xnum):
    r = xa + (xb - xa) * float(i) / (xnum - 1)
    x = startpop
    for j in range(iterations):
        x = r * x * (1. - x)
        if j > xnum / 2.:
            r_plot.append(r)
            y_plot.append(x)

plt.scatter(r_plot, y_plot, s = 1)
plt.xlabel('r')
plt.ylabel('x')
plt.show()

