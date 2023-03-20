import math
import timeit
def f(x):
    return x**5-2*x**4-5
def df(x):
    return 5*x**4-8*x**3
starttime=timeit.default_timer()
print("The start time is:",starttime)
x0=1
tolerance=1e-6
max_iterations=100
for i in range(max_iterations):
    fx=f(x0)
    dfx=df(x0)
    x1=x0-fx/dfx
    if abs(fx)<tolerance:
        print(f"Root found at x = {x1:.6f}")
        break

    else:
         x0=x1
print("The time difference is:",timeit.default_timer()-starttime)
