import argparse
import pathlib

import cooler


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=pathlib.Path, required=True)
    parser.add_argument("-o", "--output", dest="output", type=pathlib.Path, required=True)
    return parser.parse_args()

def main(args):
    args.output.parent.mkdir(parents=True, exist_ok=True)

    c = cooler.Cooler(str(args.input))
    contact = c.pixels(join=True)[:]
    contact.to_csv(args.output, sep="\t", index=False, header=False)

if __name__ == "__main__":
    main(parse_args())