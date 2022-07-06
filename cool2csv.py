import argparse
import pathlib

import cooler

from utils import import_func


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input", type=pathlib.Path, required=True)
    parser.add_argument("-o", "--output", dest="output", type=pathlib.Path, required=True)
    parser.add_argument("-m", "--multi", dest="multi", type=bool, required=True)
    parser.add_argument("-f", "--func", dest="func", type=pathlib.Path, default=None)
    return parser.parse_args()


def analyse(input: pathlib.Path, output: pathlib.Path, process_file: pathlib.Path = None):
    c = cooler.Cooler(str(input))
    contact = c.pixels(join=True)[:]
    contact = import_func.go(process_file, contact) if process_file else contact
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
            analyse(i, args.output/i.with_suffix('.csv').name, args.func)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        analyse(args.input, args.output, args.func)


if __name__ == "__main__":
    main(parse_args())