import json

import pytest


class Helpers:
    def city_code_msg(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())
        return data

    def crime_count_msg(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())
        return data


@pytest.fixture
def helpers():
    return Helpers
