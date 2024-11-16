import unittest
from matrix.matrix import (
    dotprod_std,
    dotprod_winograd,
    dotprod_winograd_optimized
)

class TestMatrixMultiplication(unittest.TestCase):
    test_cases = [
        (
            [[1]], [[2]], [[2]]
        ),
        (
            [[1, 2], [3, 4]], [[5, 6], [7, 8]], 
            [[19, 22], [43, 50]]  
        ),
        (
            [[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]], 
            [[58, 64], [139, 154]]   
        ),
        (
            [[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]], 
            [[27, 30, 33], [61, 68, 75], [95, 106, 117]]   
        )
    ]

    def check_algorithm(self, func, index):
        for a, b, res in self.test_cases:
            with self.subTest(a=a, b=b):
                if index == 0:
                    self.assertEqual(func(a, b), res)
                elif index == 1:
                    self.assertEqual(func(a, b), res)
                elif index == 2:
                    self.assertEqual(func(a, b), res)

    def test_dotprod_std(self):
        self.check_algorithm(dotprod_std, 0)

    def test_dotprod_winograd(self):
        self.check_algorithm(dotprod_winograd, 1)

    def test_dotprod_winograd_optimized(self):
        self.check_algorithm(dotprod_winograd_optimized, 2)


def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixMultiplication)
    unittest.TextTestRunner().run(suite)

