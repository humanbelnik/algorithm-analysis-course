import unittest
from algorithm.levenstein import levenstein, damerau_levenstein, levenstein_recursive, damerau_levenstein_memo

class TestDistanceAlgorithms(unittest.TestCase):
    test_cases = [
        (" ", " ", 0, 0, 0, 0),
        (" ", "qwe", 3, 3, 3, 3),
        ("qwe", " ", 3, 3, 3, 3),
        ("qweR", "QWER", 3, 3, 3, 3),
        ("qwerty", "qwertyuiop", 4, 4, 4, 4),
        ("qwer", "qwre", 2, 1, 1, 1),
        ("qwer", "qare", 3, 2, 2, 2),
        ("hello", "привет", 6, 6, 6, 6),
        ("45", "-45", 1, 1, 1, 1),
        ("qwer ber", "qwer", 4, 4, 4, 4)
    ]

    def check_algorithm(self, func, index):
        for s1, s2, lev_dist, dam_lev_iter_dist, dam_lev_rec_dist, dam_lev_memo_dist in self.test_cases:
            with self.subTest(s1=s1, s2=s2):
                if index == 0:
                    self.assertEqual(func(s1, s2)[0], lev_dist)
                elif index == 1:
                    self.assertEqual(func(s1, s2)[0], dam_lev_iter_dist)
                elif index == 2:
                    self.assertEqual(func(s1, s2), dam_lev_rec_dist)
                elif index == 3:
                    self.assertEqual(func(s1, s2), dam_lev_memo_dist)

    def test_levenstein(self):
        self.check_algorithm(levenstein, 0)

    def test_damerau_levenstein(self):
        self.check_algorithm(damerau_levenstein, 1)

    def test_levenstein_recursive(self):
        self.check_algorithm(levenstein_recursive, 2)

    def test_damerau_levenstein_memo(self):
        self.check_algorithm(damerau_levenstein_memo, 3)

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDistanceAlgorithms)
    unittest.TextTestRunner().run(suite)