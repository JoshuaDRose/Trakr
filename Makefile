#!bin/bash

setup:
	python src/install.py

cov:
	python -m coverage run -m unittest discover
	python -m coverage report -m
