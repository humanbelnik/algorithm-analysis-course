import string
import random
from time import process_time
from algorithm.levenstein import levenstein, damerau_levenstein, levenstein_recursive, damerau_levenstein_memo
import matplotlib.pyplot as plt

def run_bench():
    beg_len = 1
    end_len = 6
    n = 10

    def bench(fn):
        res = []
        
        for i in range(beg_len, end_len + 1, 1):
            tt = 0
            for j in range(n):
                print(j)
                ts = process_time()
                fn(genstr(i), genstr(i))
                te = process_time()
                tt += (te - ts)
            res.append((i, tt/n))
        return res
    
    lev = bench(levenstein)
    dam = bench(damerau_levenstein)
    dam_rec =  bench(levenstein_recursive)
    dam_memo = bench(damerau_levenstein_memo)

    vis_benchmarks(lev, dam, dam_rec, dam_memo)

def vis_benchmarks(lev, dam, dam_rec, dam_memo):
    lengths = [x[0] for x in lev]
    lev_times =[x[1] for x in lev]
    dam_times = [x[1] for x in dam]
    dam_rec_times =  [x[1] for x in dam_rec]
    dam_memo_times =[x[1] for x in dam_memo]

    print(lev_times)
    print(dam_times)
    print(dam_rec_times)
    print(dam_memo_times)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(lengths, lev_times, marker='o', color='blue', label='Левенштейн')
    plt.plot(lengths, dam_times, marker='o', color='green', label='Дамерау-Левенштейн')
    plt.plot(lengths, dam_rec_times, marker='o', color='orange', label='Рекурсивный Левенштейн')
    plt.plot(lengths, dam_memo_times, marker='o', color='red', label='Рекурсивный Дамерау-Левенштейн c мемоизацией')
    
    plt.xlabel('Длина входящих строк (Кол-во символов)')
    plt.ylabel('Время (мкс)')

    plt.legend()

    plt.title('Сравнение времени выполнения различных поиска редакционного расстояния')

    plt.grid()
    plt.show()

def genstr(l):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(l))
