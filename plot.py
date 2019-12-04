import argparse
import json
import os

import matplotlib.pyplot as plt


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def main():
    args = get_parser()

    entry = os.path.join(args.directory, "data-files.json")
    with open(entry, "r") as f:
        data = json.load(f)

    title = data["title"]

    files = [os.path.join(args.directory, f) for f in data["files"]]

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

    if args.output_file is None:
        plt.show()
    else:
        plt.savefig(args.output_file, transparent=True, bbox_inches="tight")


def get_parser():
    parser = argparse.ArgumentParser(description="Plot data")
    parser.add_argument("directory", type=str)
    parser.add_argument("-o", "--output-file", help="output image file")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
