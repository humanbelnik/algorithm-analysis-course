import unittest
import matplotlib.pyplot as plt

def linear_search(data, x):
    cmp_cnt=0
    n = len(data)
    ans=None
    for i in range(n):
        cmp_cnt+=1
        if data[i]==x:
            ans=i
            break
    return ans, cmp_cnt

def binary_search(data, x):
    cmp_cnt = 0
    ans=None
    data.sort() 

    l = 0
    r = len(data) - 1

    while l <= r:
        cmp_cnt += 1
        i_pivot = (l + r) // 2
        pivot = data[i_pivot]

        if x == pivot:
            ans=i_pivot
            break
        elif x > pivot:
            l = i_pivot + 1
        else:
            r = i_pivot - 1

    return ans, cmp_cnt
        
class TestSearchAlgorithms(unittest.TestCase):
    test_cases_linear = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, None),
        ([], 1, None),
        ([5, 4, 3, 2, 1], 1, 4),
    ]
    test_cases_binary = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, None),
        ([], 1, None),
        ([5, 4, 3, 2, 1], 1, 0),
    ]

    def check_algorithm(self, func, test_cases):
        for data, x, expected_index in test_cases:
            with self.subTest(data=data, x=x):
                self.assertEqual(func(data, x)[0], expected_index)

    def test_linear_search(self):
        self.check_algorithm(linear_search, self.test_cases_linear)

    def test_binary_search(self):
        self.check_algorithm(binary_search, self.test_cases_binary)

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchAlgorithms)
    unittest.TextTestRunner().run(suite)


def bench():
    n=1017
    data=[]
    for i in range(n): 
        data.append(i)

    lcmp=[]
    bcmp=[]

    for i in range(0,1019):
        lcmp.append(linear_search(data, i)[1])
        bcmp.append(binary_search(data, i)[1])
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 2)
    plt.bar(range(len(lcmp)), lcmp, color='black', alpha=0.7)
    plt.title('Гистограмма для Линейного поиска')
    plt.xlabel('Позиция искомого элемента в словаре')
    plt.ylabel('Количество сравнений')
    plt.ylim(-1, max(lcmp) + 1) 

    plt.subplot(1, 2, 2)
    plt.bar(range(len(bcmp)), bcmp, color='black', alpha=0.7)
    plt.title('Гистограмма для Бинарного поиска')
    plt.xlabel('Позиция искомого элемента в словаре')
    plt.ylabel('Количество сравнений')
    plt.ylim(-1, max(bcmp) + 1)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    test()
    bench()

