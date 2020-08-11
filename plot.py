import argparse
import json
import pathlib

import dufte
import matplotlib.pyplot as plt
import numpy


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


def main():
    args = get_parser()

    directory = pathlib.Path(args.directory)

    entry = directory / "data-files.json"
    with open(entry, "r") as f:
        data = json.load(f)

    title = data["title"]

    files = [directory / f for f in data["files"]]

    # read the data
    data = []
    for filename in files:
        with open(filename, "r") as f:
            data.append(json.load(f))

    # sort by the last entry in timings
    order = argsort([d["timings"][-1] for d in data])[::-1]

    plt.style.use(dufte.style)

    if args.relative:
        ref = data[order[-1]]["timings"]
        ref_name = data[order[-1]]["name"]
        for idx in order:
            d = data[idx]
            r = numpy.array(d["timings"]) / ref[: len(d["timings"])]
            plt.semilogx(d["n"], r, label=d["name"])
        plt.ylabel(f"runtime relative to {ref_name}")
        plt.ylim(0, 10)
    else:
        for idx in order:
            d = data[idx]
            plt.loglog(d["n"], d["timings"], label=d["name"])
        plt.ylabel("runtime [s]")

    dufte.legend()
    plt.title(title)
    plt.xlabel("n")

    if args.output_file is None:
        plt.show()
    else:
        plt.savefig(args.output_file, transparent=True, bbox_inches="tight")


def get_parser():
    parser = argparse.ArgumentParser(description="Plot data")
    parser.add_argument("directory", type=str)
    parser.add_argument("-o", "--output-file", help="output image file")
    parser.add_argument(
        "-r",
        "--relative",
        default=False,
        action="store_true",
        help="plot timings relative to fastest",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
