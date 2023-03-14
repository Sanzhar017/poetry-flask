install:
	poetry install

build: check
	poetry build

run: start
	python hello.py

.PHONY: install  check build