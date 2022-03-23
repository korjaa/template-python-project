"""Command-line interface module."""
import sys
import logging
import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--verbose', action="store_true",
        help="Enable verbose logging.")

    return parser.parse_args(args)


def main(args=None):
    cli_args = args if isinstance(args, list) else sys.argv[1:]
    pargs = parse_args(cli_args)

    level = logging.DEBUG if pargs.verbose else logging.INFO
    logging.basicConfig(level=level)


if __name__ == "__main__":
    main()
