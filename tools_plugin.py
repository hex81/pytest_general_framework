import os
import tempfile
import pytest

from utils.command import Command
from common.logger import logger


class HelperTrtexec:

    def __init__(self, data_path):
        self.logger = logger
        self.command = Command()
        self.data_path = data_path
        self.run_type = 'check_output'
        self.cmd = 'trtexec'

    def build_command(self, test_case):
        self.logger.info(test_case['parameters'])
        cmd_args = []
        model_file = os.path.join(self.data_path,
                                  test_case['parameters'].get('model'))

        for k, v in test_case['parameters'].items():
            if k != "model":
                if k == 'framework':
                    param = f"--{v}={model_file}"
                elif k == 'deploy':
                    deploy_file = os.path.join(self.data_path,
                                               test_case['parameters'].get('deploy'))
                    param = f"--{k}={deploy_file}"
                elif isinstance(v, bool) and v is True:
                    param = f"--{k}"
                else:
                    param = f"--{k}={v}"

                cmd_args.append(param)

        return " ".join(cmd_args)

    def run_cmd(self, test_case):
        self.cmd = " ".join([self.cmd, self.build_command(test_case)])
        self.logger.info('Run command: %s', self.cmd)
        with tempfile.TemporaryDirectory() as tmpdirname:
            result, message = self.command.run_cmd(
                tmpdirname, self.cmd, self.run_type)

        return result, message


class ToolsPlugin:
    """ Tools plugin """
    @pytest.fixture(autouse=True)
    def trtexec_helper(self, data_path):
        return HelperTrtexec(data_path)
