import argparse
from matrix.matrix import (
    read_matrix_from_file,
    print_matrix,
    dotprod_std,
    dotprod_winograd,
    dotprod_winograd_optimized,
    strassen_matrix_multiply
)

from matrix.test import test
from matrix.bench import run_bench


def parse_cmd():
    parser = argparse.ArgumentParser()
    parser.add_argument('-afile', help="Путь к файлу с первой матрицей")
    parser.add_argument('-bfile', help="Путь к файлу с второй матрицей")
    parser.add_argument('-bench', action=argparse.BooleanOptionalAction, help='Run benchmark tests')
    parser.add_argument('-test', action=argparse.BooleanOptionalAction, help='Run unit tests')  

    return parser.parse_args()

def main():
    args = parse_cmd()

    if args.test is not None:
        test()  
        exit(0)


    if args.bench is not None:
        run_bench()
        exit(0)



    a = read_matrix_from_file(args.afile)
    b = read_matrix_from_file(args.bfile)
    if len(a[0]) != len(b):
        exit(-1)

    print_matrix(dotprod_std(a, b), "standart:")
    print_matrix(dotprod_winograd(a, b), "winograd:")
    print_matrix(dotprod_winograd_optimized(a, b), "winograd optimized:")
    print_matrix(strassen_matrix_multiply(a, b), "strassen optimized:")

    
    return

if __name__ == "__main__":
    main()
