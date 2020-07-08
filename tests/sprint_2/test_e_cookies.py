from unittest import TestCase

from sprint_2.e_cookies import max_kids_with_cookies


class CookiesTest(TestCase):
    def test_both_empty(self):
        self.assertEqual(0, max_kids_with_cookies([], []))

    def test_cookies_empty(self):
        self.assertEqual(0, max_kids_with_cookies(cookies=[], kids=[1]))

    def test_kids_empty(self):
        self.assertEqual(0, max_kids_with_cookies(cookies=[1], kids=[]))

    def test_single(self):
        self.assertEqual(1, max_kids_with_cookies(kids=[1], cookies=[1]))

    def test_single_too_small(self):
        self.assertEqual(0, max_kids_with_cookies(kids=[2], cookies=[1]))

    def test_two_kids(self):
        self.assertEqual(2, max_kids_with_cookies(kids=[1, 2], cookies=[1, 2]))

    def test_two_kids_reverse(self):
        self.assertEqual(2, max_kids_with_cookies(kids=[2, 1], cookies=[2, 1]))

    def test_two_kids_mixed(self):
        self.assertEqual(2, max_kids_with_cookies(kids=[2, 1], cookies=[1, 2]))

    def test_too_many_kids(self):
        self.assertEqual(1, max_kids_with_cookies(kids=[1, 2], cookies=[1]))

    def test_too_many_cookies(self):
        self.assertEqual(3, max_kids_with_cookies(kids=[1, 2, 3], cookies=[1, 2, 3, 4]))

    def test_small_cookies(self):
        self.assertEqual(1, max_kids_with_cookies(kids=[1, 2, 3], cookies=[1, 1, 1]))

    def test_small_cookies_middle(self):
        self.assertEqual(1, max_kids_with_cookies(kids=[2, 1, 3], cookies=[1, 1, 1]))

    def test_small_cookies_end(self):
        self.assertEqual(1, max_kids_with_cookies(kids=[2, 3, 1], cookies=[1, 1, 1]))