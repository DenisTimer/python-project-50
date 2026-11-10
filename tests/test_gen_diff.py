import pytest
from pathlib import Path
from gendiff.scripts.diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.mark.parametrize("extension", ["json", "yaml", "yml"])
def test_gendiff(extension):
    file1 = get_test_data_path(f"file1.{extension}")
    file2 = get_test_data_path(f"file2.{extension}")
    expected = read_file("expected.txt")

    assert generate_diff(file1, file2) == expected