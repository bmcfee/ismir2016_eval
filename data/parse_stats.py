#!/usr/bin/env python
"""Simple utility to parse plaintext MIREX results and count the unique teams.
"""
from __future__ import print_function

import argparse
import sys


def is_teamlike(s):
    """Test a string for team-likeness.

    A string is 'teamlike' if it:
     * is uppercase
     * is alphanumeric

    Parameters
    ----------
    s : str
        Value to test.

    Returns
    -------
    valid : bool
        True if teamlike.
    """
    conds = [s.isupper(),
             s.replace("’", "").isalnum(),
             s != "MIREX",
             s != "IOACAS"]
    return all(conds)


def parse_line(s):
    """Parse the team name from a line.

    Parameters
    ----------
    s : str
        Line to parse.

    Returns
    -------
    name : str
        Returns the teamname for the line, if valid, or None.
    """
    parts = s.split()
    res = parts[0] if parts and is_teamlike(parts[0]) else None
    print(s[:10], res)
    return res


def count_teams(filename):
    """Count unique team names in a textfile.

    Parameters
    ----------
    filename : str
        Filepath to parse.

    Returns
    -------
    num : int
        Number of unique teams in the file.
    """
    runs = list(filter(None, [parse_line(l.strip()) for l in open(filename)]))
    teams = sorted(list(set(runs)))
    print("Counted {} runs from {} teams.\n[{}]"
          "".format(len(runs), len(teams), ", ".join(teams)))
    return len(teams)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("filename",
                        metavar="filename", type=str,
                        help="A textfile to parse.")

    args = parser.parse_args()
    count = count_teams(args.filename)
    sys.exit(0 if count > 0 else 1)
