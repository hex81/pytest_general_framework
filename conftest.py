# -*- coding: utf-8 -*-
# file name: conftest.py
# author: hex81
# date: 21/10/2022

import os
import yaml
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

def pytest_addoption(parser):
            parser.addoption(
            "--data-path", action="store",
            default="/mnt/data",
            help="Run samples test.")

@pytest.fixture(scope="session")
def data_path(request):
    return request.config.getoption("--data-path")

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


def pytest_generate_tests(metafunc):
    if "test_data" in metafunc.fixturenames:
        test_dir = os.path.dirname(metafunc.definition.location[0])
        test_case = os.path.basename(metafunc.definition.location[0])
        path_list = test_dir.split("/")
        for idx, element in enumerate(path_list):
            if path_list[idx] == "testcases":
                path_list[idx] = "testdata"
                break

        test_data_file = f"{test_case[:-2]}yml"
        path_list.append(test_data_file)
        data_file = os.path.join(*tuple(path_list))
        data_file = os.path.join(metafunc.config.rootdir, data_file)
        print(data_file)
        with open(data_file, "r", encoding="utf-8") as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        test_data = data.get(metafunc.definition.name)
        cases_name = [case['case_name'] for case in test_data]
        metafunc.parametrize("test_data", test_data, ids=cases_name)
