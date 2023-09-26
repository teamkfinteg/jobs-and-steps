.DEFAULT_GOAL := help

REPO_NAME ?= all
REF ?= latest

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  deps      Install python dependencies."
	@echo "  run       Run the script for a single repo if REPO_NAME and REF are set, otherwise run for all repos and latest releases."
	@echo "  build     Build the script and create a binary."
	@echo "  run-cli   Run the binary for all repos and latest releases."
	@echo "  venv      Create a virtual environment and install dependencies."

deps: venv
	bash -c "source venv/bin/activate && pip install -r requirements.txt"

venv:
	pip install virtualenv
	python3 -m venv venv
	bash -c "source venv/bin/activate && pip install --upgrade pip && pip freeze"

run:
	bash -c "source venv/bin/activate && python main.py --repo-name $(REPO_NAME) --ref $(REF)"

build:
	pip install pyinstaller
	pyinstaller --name update-store-types --onefile main.py

run-cli: build
	./dist/update-store-types --repo-name $(REPO_NAME) --ref $(REF)

quickstart: deps run
	cat store_types.json

.PHONY: help deps run run-cli venv quickstart