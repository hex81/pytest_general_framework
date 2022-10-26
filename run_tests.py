"""
test
"""
# run test all
#

import sys
import argparse
import pytest

from samples_plugin import SamplesPlugin

def main():
    parser = argparse.ArgumentParser(description='Parse test parameters.')
    parser.add_argument('--samples-path', action='store',
                        help='Run samples.')

    args = parser.parse_args()

    params = ["-s"]
    if args.samples_path:
        params.append(f"--samples-path={args.samples_path}")
        params.append("-m samplestest")

    pytest.main(params, plugins=[SamplesPlugin()])

if __name__ == "__main__":
    sys.exit(main())
