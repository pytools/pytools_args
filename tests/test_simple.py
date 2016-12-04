# -*- coding: utf-8 -*-

import unittest
from .context import pytools_args as args


class CustomArgHandler(args.ArgumentHandler):

    def check(self):
        if args.has_args() and args.get_main_arg() == 1:
            return True

    def handle(self):
        return 42


class TestSimpleCases(unittest.TestCase):

    def test_empty_call(self):
        args.set_arg_processor(lambda: ([]))

        self.assertFalse(args.passed())

        self.assertFalse(args.has_args())
        self.assertFalse(args.has_main_arg())
        self.assertFalse(args.has_sub_args())

        self.assertEqual(args.num_args(), 0)
        self.assertEqual(args.num_sub_args(), 0)

        self.assertEqual(args.get_args(), None)
        self.assertEqual(args.get_main_arg(), None)

        self.assertEqual(args.get_sub_args(), None)
        self.assertEqual(args.get_sub_arg(0), None)
        self.assertEqual(args.get_sub_arg(1), None)
        self.assertEqual(args.get_sub_arg(2), None)

    def test_one_arg(self):
        args.set_arg_processor(lambda: ([1]))

        self.assertTrue(args.passed())

        self.assertTrue(args.has_args())
        self.assertTrue(args.has_main_arg())
        self.assertFalse(args.has_sub_args())

        self.assertEqual(args.num_args(), 1)
        self.assertEqual(args.num_sub_args(), 0)

        self.assertListEqual(args.get_args(), [1])
        self.assertEqual(args.get_main_arg(), 1)

        self.assertEqual(args.get_sub_args(), None)
        self.assertEqual(args.get_sub_arg(0), None)
        self.assertEqual(args.get_sub_arg(1), None)
        self.assertEqual(args.get_sub_arg(2), None)

    def test_two_args(self):
        args.set_arg_processor(lambda: ([1, 2]))

        self.assertTrue(args.passed())

        self.assertTrue(args.has_args())
        self.assertTrue(args.has_main_arg())
        self.assertTrue(args.has_sub_args())

        self.assertEqual(args.num_args(), 2)
        self.assertEqual(args.num_sub_args(), 1)

        self.assertListEqual(args.get_args(), [1, 2])
        self.assertEqual(args.get_main_arg(), 1)

        self.assertEqual(args.get_sub_args(), [2])
        self.assertEqual(args.get_sub_arg(0), 2)
        self.assertEqual(args.get_sub_arg(1), None)
        self.assertEqual(args.get_sub_arg(2), None)

    def test_three_args(self):
        args.set_arg_processor(lambda: ([1, 2, 3]))

        self.assertTrue(args.passed())

        self.assertTrue(args.has_args())
        self.assertTrue(args.has_main_arg())
        self.assertTrue(args.has_sub_args())

        self.assertEqual(args.num_args(), 3)
        self.assertEqual(args.num_sub_args(), 2)

        self.assertListEqual(args.get_args(), [1, 2, 3])
        self.assertEqual(args.get_main_arg(), 1)

        self.assertEqual(args.get_sub_args(), [2, 3])
        self.assertEqual(args.get_sub_arg(0), 2)
        self.assertEqual(args.get_sub_arg(1), 3)
        self.assertEqual(args.get_sub_arg(2), None)

    def test_arg_handlers(self):
        args.set_arg_processor(lambda: ([1, 2, 3]))
        args.add_handler(CustomArgHandler())

        self.assertEqual(args.handle_args(), 42)

if __name__ == '__main__':
    unittest.main()
