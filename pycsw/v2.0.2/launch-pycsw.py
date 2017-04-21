#!/usr/bin/env python
"""A docker entrypoint script for launching pycsw.

This script will either execute pycsw-admin or launch pycsw's wsgi server
It uses `pysu` in order to drop privileges when executing.

"""

import argparse
import logging
import sys

from pysu import cli


def prepare_pycsw_server_command(*args):
    return ["python", "-m", "pycsw.wsgi"]


def prepare_pycsw_admin_command(*args):
    return ["pycsw-admin.py", "-f", "/etc/pycsw/pycsw.cfg", "-c"] + list(args)


def _get_parser(description=__doc__):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--pysu-user",
        default="1000:1000",
        help=("User to change to with python-su. Can also be specified as "
              "user:group")
    )
    subparsers = parser.add_subparsers(
        help=("Either run pycsw standalone or perform maintenance tasks with "
              "pycsw-admin")
    )
    parser_admin = subparsers.add_parser(
        "admin",
        help="Run 'pycsw-admin'. Any extra arguments are passed directly to "
             "pycsw-admin. Example: 'launch_pycsw user admin "
             "-f /etc/pycsw/pycsw.cfg -c setup_db'"
    )
    parser_admin.set_defaults(func=prepare_pycsw_admin_command)
    parser_run = subparsers.add_parser(
        "run",
        help="Run the pycsw `pycsw.wsgi` module."
    )
    parser_run.set_defaults(func=prepare_pycsw_server_command)
    return parser


if __name__ == "__main__":
    parser = _get_parser()
    args, unkwnown_args = parser.parse_known_args()
    command_to_excute = args.func(*unkwnown_args)
    sys.argv = [sys.argv[0], args.pysu_user] + command_to_excute
    cli.main()
