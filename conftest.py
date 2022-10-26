# -*- coding: utf-8 -*-
# file name: conftest.py
# author: hex81
# date: 21/10/2022

import os
import subprocess
import pytest


@pytest.fixture
def arch():
    return "x86"


@pytest.fixture(autouse=True)
def skip_by_arch(request, arch):
    """
    skip arch
    """
    if request.node.get_closest_marker('skip_arch'):
        if request.node.get_closest_marker('skip_arch').args[0] == arch:
            pytest.skip(f'skipped on this arch: {arch}')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_arch(arch): skip test for the given search engine",
    )


def pytest_runtest_setup(item):
    """
    test cases setup, config logger.
    Args:
        item:
    Returns:
    """
    config = item.config
    # log_dir = item.location[0].rsplit("/", 1)[0]
    log_dir = config.rootpath
    logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
    report_file = os.path.join(f"{log_dir}/logs",
                               f"{item._request.node.name}.log")
    logging_plugin.set_log_path(report_file)
