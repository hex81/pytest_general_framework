"""
Run cmd
"""

import subprocess

from common.logger import logger

class Command:
    """ This class is used to run command """

    @staticmethod
    def run_cmd(path, cmd, run_type='check_output'):
        """
            Args:
                path: command path
                cmd: command
                caller: subprocess method. run, check_output
            Return:
                bool & message
        """

        logger.info('Start to run %s under %s', cmd, path)

        caller = getattr(subprocess, run_type)
        message = ''

        try:
            res = caller(f"cd {path}; {cmd}",
                stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as call_e:
            if run_type == "check_output":
                message = call_e.output.decode(encoding="utf-8")
                logger.error(message)
            return False, message
        else:
            if run_type == "check_output":
                message = res.decode(encoding="utf-8")
                logger.info(message)

        return True, message
