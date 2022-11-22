import os

from .command import Command

def get_cuda_version(cuda_path='/usr/local/cuda'):
    """Utility function to get cuda version

    Parameters
    ----------
    cuda_path : str
        Path to cuda root.

    Returns
    -------
    version : float
        The cuda version
    """

    cmd = "nvcc --version | grep release | awk -F, '{print $2}'"
    result, message = Command().run_cmd(cuda_path, cmd)
    if result:
        return float(message.strip().split()[1])
    else:
        raise RuntimeError('Could not get cuda version.')
