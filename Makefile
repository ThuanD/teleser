.PHONY: init build test run-hooks update-deps

init:
	poetry install --all-extras

build:
	poetry build

test:
	poetry run coverage run -m pytest
	poetry run coverage html

run-hooks:
	poetry run pre-commit run --all-files --show-diff-on-failure

update-deps:
	poetry update
