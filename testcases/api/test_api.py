"""
API test suite
"""

import pytest

from common.logger import logger


class TestAPI:

    def test_api_example(self):
        logger.info('test on example')

    def test_api_smoke(self):
        logger.info('test on smoke')

    @pytest.mark.skip_arch('x86')
    def test_api_skip_x86(self):
        logger.info('test on x86')

    @pytest.mark.skip_arch('sbsa')
    def test_api_skip_sbsa(self):
        logger.info('test on sbsa')
