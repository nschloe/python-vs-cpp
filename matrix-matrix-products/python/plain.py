import numpy
import time

r = 1
for k in range(15):
    n = 2 ** k
    u = [
        numpy.random.rand(n).tolist()
        for _ in range(n)
    ]
    v = [
        numpy.random.rand(n).tolist()
        for _ in range(n)
    ]
    t = 1.0e+10  # something huge
    for _ in range(r):
        out = [
            numpy.random.rand(n).tolist()
            for _ in range(n)
        ]
        t0 = time.time_ns()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    out[i][j] += u[i][k] * v[k][j]
        t1 = time.time_ns()
        t = min(t, t1 - t0)

    t *= 1.0e-9
    print(f"{t:.6e}, ")
