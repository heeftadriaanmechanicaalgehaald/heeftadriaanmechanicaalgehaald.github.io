import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy


def planck(x, a, b, c):
    return a * np.power(x, 3) * (1 / (np.exp(x * b) - 1)) + c


def linear(x, a, b, c):
    return a * x + b + c


def taylor(x, a, b, c):
    return a * x**2 + b * x + c


def xsinx(x, a, b, c):
    return c * (scipy.special.gamma(a * x)) / (np.exp(b * x**2))


def fit_stuff(f, cijfers):
    x_continuous = np.linspace(1, len(cijfers) + 2, 1000)
    params, _ = curve_fit(f, xs, cijfers)
    prediction = f(len(cijfers) + 1, params[0], params[1], params[2])
    tentamen_halen = -1
    for i in range(1, 100):
        if f(i + 1, params[0], params[1], params[2]) > 5.5:
            tentamen_halen = i
            break
    return (
        prediction,
        tentamen_halen,
        x_continuous,
        f(x_continuous, params[0], params[1], params[2]),
    )


cijfers = [1.8, 1.4, 3.5, 5.2, 2.5, 2, 6.0]
xs = list(range(1, len(cijfers) + 1))


plt.scatter(xs, cijfers, label="Daadwerkelijke cijfers")
plt.scatter((8), (6.0), label="Adriaan's eigen voorspelling")

prediction, tentamen_halen, x_continuous, cijfers_continuous = fit_stuff(
    planck, cijfers
)
print(prediction, tentamen_halen)
plt.plot(x_continuous, cijfers_continuous, label="Planck fit")

prediction, tentamen_halen, x_continuous, cijfers_continuous = fit_stuff(
    linear, cijfers
)
print(prediction, tentamen_halen)
plt.plot(x_continuous, cijfers_continuous, label="Linear fit")

prediction, tentamen_halen, x_continuous, cijfers_continuous = fit_stuff(
    taylor, cijfers
)
print(prediction, tentamen_halen)
plt.plot(x_continuous, cijfers_continuous, label="Taylor fit")

# prediction, tentamen_halen, x_continuous, cijfers_continuous = fit_stuff(xsinx, cijfers)
# print(prediction, tentamen_halen)
# plt.plot(x_continuous, cijfers_continuous, label="XsinX fit")


plt.legend()
plt.ylim(0, 10)
plt.xlabel("De hoeveelste pogin het is")
plt.ylabel("Het cijfer van het tentamen")
plt.show()
