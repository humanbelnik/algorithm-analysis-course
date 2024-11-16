import random
from time import process_time
import matplotlib.pyplot as plt
from matrix.matrix import dotprod_std, dotprod_winograd, dotprod_winograd_optimized

def run_bench():
    beg_len = 1
    end_len = 301
    step = 10
    n = 1 

    def gen_matrix(size):
        return [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

    def bench(fn):
        res = []
        
        for size in range(beg_len, end_len + 1, step):
            total_time = 0
            for _ in range(n):
                a = gen_matrix(size)
                b = gen_matrix(size)
                
                start_time = process_time()
                fn(a, b)
                end_time = process_time()
                
                total_time += (end_time - start_time)
            res.append((size, total_time / n))
        return res
    
    std_times = bench(dotprod_std)
    winograd_times = bench(dotprod_winograd)
    winograd_opt_times = bench(dotprod_winograd_optimized)

    vis_benchmarks(std_times, winograd_times, winograd_opt_times)

def vis_benchmarks(std_times, winograd_times, winograd_opt_times):
    sizes = [x[0] for x in std_times]
    std_exec_times = [x[1] for x in std_times]
    winograd_exec_times = [x[1] for x in winograd_times]
    winograd_opt_exec_times = [x[1] for x in winograd_opt_times]

    print(f"{'Размер матрицы':<15} | {'Стандартный':<15} | {'Виноград':<15} | {'Оптимизированный Виноград':<25}")
    print("-" * 75)
    for size, std_time, winograd_time, winograd_opt_time in zip(sizes, std_exec_times, winograd_exec_times, winograd_opt_exec_times):
        print(f"{size:<15} | {std_time:<15.6f} | {winograd_time:<15.6f} | {winograd_opt_time:<25.6f}")
    
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, std_exec_times, marker='o', color='blue', label='Стандартный алгоритм')
    plt.plot(sizes, winograd_exec_times, marker='s', color='green', label='Алгоритм Винограда')
    plt.plot(sizes, winograd_opt_exec_times, marker='^', color='red', label='Оптимизированный алгоритм Винограда')

    plt.xlabel('Линейный размер матрицы (элементы)')
    plt.ylabel('Время выполнения (секунды)')

    plt.legend()

    plt.title('Сравнение времени выполнения алгоритмов умножения матриц')

    plt.grid()
    plt.show()
