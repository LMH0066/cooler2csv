import argparse
import pathlib

import cooler


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=pathlib.Path, required=True)
    parser.add_argument("-o", "--output", dest="output", type=pathlib.Path, required=True)
    parser.add_argument("-m", "--multi", dest="multi", type=bool, required=True)
    return parser.parse_args()


def analyse(input: pathlib.Path, output: pathlib.Path):
    c = cooler.Cooler(str(input))
    contact = c.pixels(join=True)[:]
    contact.to_csv(output, sep="\t", index=False, header=True)


def main(args):
    if args.multi:
        if not args.input.is_dir():
            raise RuntimeError("input is not a folder path")
        
        args.output.mkdir(parents=True, exist_ok=True)
        for i in args.input.iterdir():
            if not i.is_file():
                print("{} is not a file".format(i))
                continue
            analyse(i, args.output/i.with_suffix('.csv').name)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        analyse(args.input, args.output)


if __name__ == "__main__":
    main(parse_args())