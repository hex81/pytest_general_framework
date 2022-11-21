"""
sample test suite
"""

import pytest


CPP_SAMPLES = [
    "sample_algorithm_selector", "sample_char_rnn",
    "sample_dynamic_reshape", "sample_int8_api",
    "sample_io_formats", "sample_onnx_mnist"]


@pytest.mark.samples
@pytest.mark.usefixtures("prepare")
class TestSamples:

    # @pytest.fixture(autouse=True)
    # def _init_helper(self, samples_path):
    #     self._helper = HelperSamples(samples_path)

    @pytest.mark.parametrize('sample', CPP_SAMPLES)
    def test_cpp_samples(self, samples_helper,  sample):
        result, message = samples_helper.run_cmd("../bin", f"{sample}")
        assert result, message

    def test_python_samples_network_api_pytorch_mnist(self, samples_helper):
        result, message = samples_helper.run_cmd(
            "python/network_api_pytorch_mnist", "sample.py")
        assert result, message
