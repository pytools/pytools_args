# -*- coding: utf-8 -*-

import unittest
from .context import pytools_args


class TestSimpleCases(unittest.TestCase):

    def test_existence(self):
        self.assertTrue(hasattr(pytools_args, '__mock'))


if __name__ == '__main__':
    unittest.main()
