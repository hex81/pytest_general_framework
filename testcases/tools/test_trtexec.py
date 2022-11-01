"""
trtexec test suite
"""

import pytest

from helper.tools.helper_trtexec import HelperTrtexec


class TestTrtexec:
    """Test trtexec"""

    @pytest.fixture(autouse=True)
    def _init_helper(self, data_path):
        self._helper = HelperTrtexec(data_path)

    def test_trtexec(self, test_data):
        self._helper.run_cmd(test_data)
