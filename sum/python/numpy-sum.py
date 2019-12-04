import time

import numpy

r = 100
for k in range(27):
    n = 2 ** k
    u = numpy.random.rand(n)
    t = 1.0e10  # something huge
    for _ in range(r):
        t0 = time.time_ns()
        out = numpy.sum(u)
        t1 = time.time_ns()
        t = min(t, t1 - t0)

    t *= 1.0e-9
    print(f"{t:.6e}, ")
