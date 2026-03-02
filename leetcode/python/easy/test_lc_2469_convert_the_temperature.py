import math
from lc_2469_convert_the_temperature import solve


def test_example_1():
    celsius = 36.50
    ans = solve(celsius)
    print(f"Temperatura de {celsius:.2f} Celsius convertida para Kelvin é {ans[0]:.2f} e para Fahrenheit é {ans[1]:.2f}.")
    assert math.isclose(ans[0], 309.65, abs_tol=1e-5)
    assert math.isclose(ans[1], 97.70, abs_tol=1e-5)


def test_example_2():
    celsius = 122.11
    ans = solve(celsius)
    print(f"Temperatura de {celsius:.2f} Celsius convertida para Kelvin é {ans[0]:.2f} e para Fahrenheit é {ans[1]:.3f}.")
    assert math.isclose(ans[0], 395.26, abs_tol=1e-5)
    assert math.isclose(ans[1], 251.798, abs_tol=1e-5)
