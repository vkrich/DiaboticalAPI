import unittest
from main import check_arguments, get_request
import argparse


class TestCases(unittest.TestCase):

    def test_check_arguments_1(self):
        result = check_arguments(argparse.Namespace(mode="r_ca_2", count=1))
        self.assertEqual(result, True)

    def test_get_request_1(self):
        result = get_request(argparse.Namespace(mode='r_wo', count=2, country='ru', user_id=None))
        self.assertEqual(result, 0)

    def test_get_request_2(self):
        result = get_request(argparse.Namespace(mode='r_wo', count=1, country=None, user_id=None))
        self.assertEqual(result, [{'name': '2z Silencep', 'country': 'nl', 'match_type': 2,
                                   'rating': '2232', 'rank_tier': 40, 'rank_position': 1, 'match_count': 81,
                                   'match_wins': 66}])


if __name__ == '__main__':
    unittest.main()