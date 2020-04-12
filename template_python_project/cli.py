"""This module defines CLI interface
"""
import sys
import logging
import argparse


def parse_args(args):
    """Parses given arguments.
    This function is separated from main for testing purposes.
    https://stackoverflow.com/questions/18160078/how-do-you-write-tests-for-the-argparse-portion-of-a-python-module
    Arguments:
        args {list} -- List of arguments.
    Returns:
        [type] -- Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument(
        '--verbose', action="store_true",
        help="Enable verbose logging")

    parser.add_argument(
        '--multi', type=str, choices=["op1", "op2"], default="op1",
        help='Example choices selection')

    return parser.parse_args(args)


def main(args=None):
    """Executes CLI interface.
    """

    # Parse arguments
    # ---------------
    if isinstance(args, list):
        # parse_args being is being tested.
        pargs = parse_args(args)
    else:
        pargs = parse_args(sys.argv[1:])

    if pargs.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
