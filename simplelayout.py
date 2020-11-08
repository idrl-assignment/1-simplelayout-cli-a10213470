import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--board_grid", type=int)
    parser.add_argument("--unit_grid", type=int)
    parser.add_argument("--unit_n", type=int)
    parser.add_argument("--positions", type=int, nargs='+')
    parser.add_argument("--outdir", type=str)
    parser.add_argument("--file_name", type=str)
    args = parser.parse_args()
    if args.board_grid % args.unit_grid != 0:
        sys.exit()
    if len(args.positions) != args.unit_n:
        sys.exit()
    for i in args.positions:
        if i < 1 or i > (args.board_grid/args.unit_grid)**2:
            sys.exit()
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    with open(args.outdir + '/' + args.file_name + '.jpg', 'r') as _:
        pass
    with open(args.outdir + '/' + args.file_name + '.mat', 'r') as _:
        pass


if __name__ == "__main__":
    main()
