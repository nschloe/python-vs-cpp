import os
import json
import matplotlib.pyplot as plt


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def main():
    entry = "dot-product/data-files.json"
    with open(entry, "r") as f:
        data = json.load(f)

    title = data["title"]

    files = [os.path.join("dot-product", f) for f in data["files"]]

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
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("runtime [s]")
    plt.show()


if __name__ == "__main__":
    main()
