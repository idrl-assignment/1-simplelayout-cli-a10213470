import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_grid", help="display a square of a given number",
                    type=int)
    parser.add_argument("unit_grid", help="display a square of a given number",
                    type=int)
    parser.add_argument("unit_n", help="display a square of a given number",
                    type=int)
    parser.add_argument("unit_n", help="display a square of a given number",
                    type=list)
    parser.add_argument("outdir", help="display a square of a given number",
                    type=str)
    parser.add_argument("file_name", help="display a square of a given number",
                    type=str)
    args = parser.parse_args()
    print(args.square**2)

if __name__ == "__main__":
    main()
