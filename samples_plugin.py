'''
samples plugin
'''

import pytest
import os

from utils.command import Command
from common.logger import logger


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


class SamplesPlugin:
    """ Samples plugin """

    def pytest_addoption(self, parser):
        parser.addoption(
            "--samples-path", action="store",
            help="Run samples test.")

    def pytest_configure(self, config):
        config.addinivalue_line(
            "markers", "samples: this one is for samples tests.")

    def pytest_collection_modifyitems(self, config, items):
        if not config.getoption("--samples-path"):
            skip_samples = pytest.mark.skip(
                reason="need --samples-path option to run")
            for item in items:
                if item.get_closest_marker("samples"):
                    item.add_marker(skip_samples)

    @pytest.fixture(scope="session")
    def samples_path(self, request):
        return request.config.getoption("--samples-path")

    @pytest.fixture(scope="session")
    def prepare(self, samples_path):
        """
        Get sample list
        """

        result, mesg = Command.run_cmd(
            path=samples_path, cmd="make", run_type='run')
        if not result:
            raise Exception("Compile samples failure.")

        result, mesg = Command.run_cmd(path=f"{samples_path}/../python",
                                       cmd="./python_setup.sh", run_type='run')
        if not result:
            raise Exception("python setup failure.")

    @pytest.fixture(autouse=True)
    def samples_helper(self, samples_path):
        return HelperSamples(samples_path)

    # def pytest_generate_tests(self, metafunc):
    #     samples_path = metafunc.config.getoption('--samples-path')
    #     if "sample" in metafunc.fixturenames:

    #         self.compile_samples(samples_path)

    #         cmd = f"cd {samples_path}/../bin; ls | grep sample | grep -v debug"
    #         try:
    #             res = subprocess.check_output(cmd, shell=True)
    #         except subprocess.CalledProcessError as call_e:
    #             print(call_e.output.decode(encoding="utf-8"))
    #         else:
    #             samples = res.decode(encoding='utf-8').strip().split("\n")

    #         metafunc.parametrize("sample", samples)
