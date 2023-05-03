.PHONY: clean install_requirements install build upload

clean:
	rm -rf dist/
	rm -rf build/
	rm -rf poetry.lock
	rm -rf src/pypbgpasn.egg-info/

install_requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

install:
	poetry install

build:
	poetry build

upload:
	python3 -m pip install --upgrade twine
	python3 -m twine upload --repository pypi dist/*