"""
samples helper
"""

from common.logger import logger
from utils.command import Command

import os


class HelperSamples:

    def __init__(self, sample_path):
        self.logger = logger
        self.command = Command()
        self.sample_path = sample_path
        self.run_type = 'check_output'

    def run_cmd(self, path, cmd):
        self.logger.info('Run sample %s', cmd)
        run_path = os.path.join(self.sample_path, path)
        if "python" in run_path:
            cmd = f"pip3 install -r requirements.txt && python3 {cmd}"

        result, message = self.command.run_cmd(run_path, cmd, self.run_type)

        return result, message
