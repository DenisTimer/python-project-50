.PHONY: demo lint build

demo:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

lint:
	uv run ruff check gendiff

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff