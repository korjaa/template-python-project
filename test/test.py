"""This module defines unittests for the Python project
"""
import unittest
import template_python_project


class TestArgs(unittest.TestCase):
    """This class tests elasticsearch login
    Extends:
        unittest.TestCase
    """

    def setUp(self):
        pass

    def test_verbose_false(self):
        """Test argument parser missing --verbose option
        """
        pargs = template_python_project.cli.parse_args([])
        self.assertFalse(pargs.verbose)

    def test_verbose_true(self):
        """Test argument parser included --verbose option
        """
        pargs = template_python_project.cli.parse_args(["--verbose"])
        self.assertTrue(pargs.verbose)
