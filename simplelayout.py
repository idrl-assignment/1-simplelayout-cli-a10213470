import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("board_grid", type=int)
    parser.add_argument("unit_grid", type=int)
    parser.add_argument("unit_n", type=int)
    parser.add_argument("positions", type=int, nargs='+')
    parser.add_argument("outdir", default='\example_dir', type=str)
    parser.add_argument("file_name", default='example', type=str)
    args = parser.parse_args()
    if args.board_grid % args.unit_grid !=0: 
        SystemExit()
    if len(positions)!= unit_n: 
        SystemExit()
    for i in args.positions: 
        if i<0 or i>(args.board_grid/args.unit_grid)^2: 
            SystemExit()
    with open(args.outdir+'/'+ args.file_name, 'r') as f1:  
    

if __name__ == "__main__":
    main()
