venv:
	-rm -rf venv
	virtualenv -p python3 venv

install:
	venv/bin/pip install -r requirements.txt

test:
	venv/bin/python -m unittest discover

requirements:
	pip freeze > requirements.txt

release-major:
	bumpversion major

release-minor:
	bumpversion minor

release-patch:
	bumpversion patch

clean:
	-ln -sfn ~/vagrant/.pypirc ~/.pypirc
	-rm -rf build
	-rm -rf dist

register:
	make clean
	python setup.py sdist bdist_wheel
	twine register dist/*.whl

upload:
	make clean
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: venv install test requirements clean register upload
