from pathlib import Path
from gendiff.scripts.diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff():
    expected_value = read_file("expected.txt")
    file1 = get_test_data_path("file1.json")
    file2 = get_test_data_path("file2.json")
    actual_value = generate_diff(file1, file2)
    assert actual_value == expected_value