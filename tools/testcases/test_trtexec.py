"""
trtexec test suite
"""

import pytest


class TestTRTexec:
    """Test trtexec"""

    def test_trtexec(self, trtexec_helper, test_data):
        result, message = trtexec_helper.run_cmd(test_data)
        assert result, message
