import time

import numpy

r = 1
for k in range(27):
    n = 2 ** k
    u = numpy.random.rand(n).tolist()
    v = numpy.random.rand(n).tolist()
    t = 1.0e10  # something huge
    for _ in range(r):
        t0 = time.time_ns()
        out = 0.0
        for uu, vv in zip(u, v):
            out += uu * vv
        t1 = time.time_ns()
        t = min(t, t1 - t0)

    t *= 1.0e-9
    print(f"{n} {t:.6e}")
