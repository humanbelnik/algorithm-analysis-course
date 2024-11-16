import argparse
from algorithm.levenstein import (
    levenstein,
    damerau_levenstein,
    levenstein_recursive,
    damerau_levenstein_memo,
    levensteinTrace
)
from algorithm.bench import run_bench
from algorithm.test import test
from matrix.matrix import matrix_print

def parse_args() -> any:
    parser = argparse.ArgumentParser()
    parser.add_argument('--wmat', action=argparse.BooleanOptionalAction, help='Show matrix output')
    parser.add_argument('--bench', action=argparse.BooleanOptionalAction, help='Run benchmark tests')
    parser.add_argument('--test', action=argparse.BooleanOptionalAction, help='Run unit tests')  

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    with_matrix = args.wmat
    with_bench = args.bench
    with_test = args.test 

    if with_test is not None:
        test()  
        exit(0)


    if with_bench is not None:
        run_bench()
        exit(0)

    s1, s2 = input("1st string="), input("2nd string=")
    lev, lev_matrix = levenstein(s1, s2)
    dlev, dlev_matrix = damerau_levenstein(s1, s2)
    dlev_rec = levenstein_recursive(s1, s2)
    dlev_memo = damerau_levenstein_memo(s1, s2)


    print(
        ">>\n"
        f"Non-recursive Levenstein={lev}\n"
        f"Non-recursive Damerau-Levenstein={dlev}\n"
        f"Recursive Levenstein={dlev_rec}\n"
        f"Memoized Damerau-Levenstein={dlev_memo}\n"
    )

    if with_matrix is not None:
        matrix_print(lev_matrix, prompt="Matrix of Levenstein's algorithm:")
        #matrix_print(dlev_matrix, prompt="Matrix of Damerau-Levenstein's algorithm:") 
    print(f"trace: {levensteinTrace(lev_matrix, s1, s2)}")   
