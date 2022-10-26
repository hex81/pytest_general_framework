"""
sample test suite
"""

import pytest

from common.logger import logger
from helper.samples.helper_samples import HelperSamples



@pytest.mark.samplestest
class TestSamples:

    @pytest.fixture(autouse=True)
    def _init_helper(self, samples_path):
        logger.info(f'sample path is {samples_path}')
        self._helper = HelperSamples(samples_path)


    def test_cpp_samples(self, sample):
        result, message = self._helper.run_sample(f"sudo ./{sample}")
        assert result, message
