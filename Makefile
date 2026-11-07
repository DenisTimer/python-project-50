.PHONY: demo lint build

demo:
	uv run gendiff raw-data/file1.json raw-data/file2.json

lint:
	uv run ruff check gendiff

build:
	uv build