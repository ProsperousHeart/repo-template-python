lint:
	flake8 src/ test/

format:
	black src/ test/

test:
	pytest -v
