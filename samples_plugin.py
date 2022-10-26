'''
samples plugin
'''

import re
import subprocess
import pytest


class SamplesPlugin:
    """ Samples plugin """

    def pytest_addoption(self, parser):
        parser.addoption(
            "--samples-path", action="store",
            default="/home/tensorrt/samples",
            help="Run samples test.")

    def pytest_configure(self, config):
        config.addinivalue_line("markers", "samplestest: this one is for samples tests.")

    @pytest.fixture(scope="session")
    def samples_path(self, request):
        return request.config.getoption("--samples-path")

    def compile_samples(self, samples_path):
        """
        Get sample list
        """

        cmd = f"cd {samples_path}; sudo make"

        try:
            subprocess.run(cmd, shell=True, check=True)
        except subprocess.CalledProcessError as call_e:
            print(call_e.output.decode(encoding="utf-8"))
            return False

        return True

    def pytest_generate_tests(self, metafunc):
        samples_path = metafunc.config.getoption('--samples-path')
        if "sample" in metafunc.fixturenames:

            self.compile_samples(samples_path)

            cmd = f"cd {samples_path}/../bin; ls | grep sample | grep -v debug"
            try:
                res = subprocess.check_output(cmd, shell=True)
            except subprocess.CalledProcessError as call_e:
                print(call_e.output.decode(encoding="utf-8"))
            else:
                samples = res.decode(encoding='utf-8').strip().split("\n")

            metafunc.parametrize("sample", samples)
