.PHONY: all test

all:
	cd src/ && python main.py

test:
	cd src/ && python -m unittest -v