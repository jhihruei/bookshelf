.PHONY: install
install:
	python3 -m pip install -r requirements.txt
	python3 -m pip install -r requirements-dev.txt

.PHONY: start
start:
	python3 -m flask run -p 3000

.PHONY: format
format:
	python3 -m isort .
	python3 -m black .

.PHONY: pylint
pylint:
	python3 -m pylint --rcfile=.pylintrc --disable=C,R,W *.py
