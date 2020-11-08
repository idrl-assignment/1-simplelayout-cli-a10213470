import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_grid", help="the board grid",
                    type=int)
    parser.add_argument("unit_grid", help="the unit grid",
                    type=int)
    parser.add_argument("unit_n", help="the number of unit",
                    type=int)
    parser.add_argument(
                    "positions", 
                    help="the positions of every unit", 
                    type=list)
    parser.add_argument("outdir", help="the output directory",
                    type=str)
    parser.add_argument("file_name", help="the file name",
                    type=str)
    args = parser.parse_args()
    print(args.square**2)
    if args.board_grid % args.unit_grid !=0:
        SystemExit()



if __name__ == "__main__":
    main()
