"""
Run cmd
"""

import subprocess

def run_cmd(test_dir, cmd):
    try:
        res = subprocess.check_output(f"cd {test_dir}; {cmd}",
            shell=True)
    except subprocess.CalledProcessError as call_e:
        message = call_e.output.decode(encoding="utf-8")
        return False, message
    else:
        message = res.decode(encoding="utf-8")

    return True, message
