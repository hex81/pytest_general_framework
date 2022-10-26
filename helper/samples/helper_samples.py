"""
samples helper
"""

from common.logger import logger
from utils.run_cmd import run_cmd

class HelperSamples:

    def __init__(self, sample_path):
        self.logger = logger
        self.sample_path = sample_path
        self.bin_path = f"{sample_path}/../bin"

    def run_sample(self, cmd):
        self.logger.info(f'Run sample: {cmd}')
        result, message = run_cmd(self.bin_path, cmd)

        if result:
            self.logger.info(message)
        else:
            self.logger.error(message)
        
        return result, message
