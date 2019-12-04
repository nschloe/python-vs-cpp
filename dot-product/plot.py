import json
import matplotlib.pyplot as plt

files = [
    "cpp/eigen.json",
    "cpp/plain.json",
    "python/plain.json",
    "python/numpy.json",
]


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


# read the data
data = []
for filename in files:
    with open(filename, "r") as f:
        data.append(json.load(f))

# sort by the last entry in timings
order = argsort([d["timings"][-1] for d in data])[::-1]

for idx in order:
    d = data[idx]
    plt.loglog(d["n"], d["timings"], label=d["name"])

plt.grid()
plt.legend()
plt.title("dot product")
plt.xlabel("n")
plt.ylabel("runtime [s]")
plt.show()
