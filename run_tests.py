"""
test
"""
# run test all
#

import sys
import argparse
import pytest

from samples_plugin import SamplesPlugin
from tools_plugin import ToolsPlugin


def main():
    parser = argparse.ArgumentParser(description='Parse test parameters.')
    parser.add_argument('--samples-path', action='store',
                        help='Run samples.')
    parser.add_argument('--test-plan', action='store',
                        help='Run test plan.')

    args = parser.parse_args()

    params = ["-s"]
    if args.samples_path:
        params.append(f"--samples-path={args.samples_path}")

    if args.test_plan:
        params.append(f"--test-plan={args.test_plan}")

    params.append(f"--junit-xml=result.xml")

    pytest.main(params, plugins=[SamplesPlugin(), ToolsPlugin()])


if __name__ == "__main__":
    sys.exit(main())
