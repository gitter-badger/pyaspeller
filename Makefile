# Some simple testing tasks (sorry, UNIX only).

FLAGS=


flake:
#	python setup.py check -rms
	flake8 pyaspeller tests examples

develop:
	python setup.py develop

test: flake develop
	nosetests -s $(FLAGS) ./tests/

vtest: flake develop
	nosetests -s -v $(FLAGS) ./tests/


cov cover coverage: flake
	coverage run --source=pyaspeller setup.py test && coverage report

cov-dev: flake develop
	@coverage erase
	@coverage run -m nose -s $(FLAGS) tests
	@mv .coverage .coverage.accel
	@pyaspeller_NO_EXTENSIONS=1 coverage run -m nose -s $(FLAGS) tests
	@mv .coverage .coverage.pure
	@coverage combine
	@coverage report
	@coverage html
	@echo "open file://`pwd`/coverage/index.html"

clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -f `find . -type f -name '@*' `
	rm -f `find . -type f -name '#*#' `
	rm -f `find . -type f -name '*.orig' `
	rm -f `find . -type f -name '*.rej' `
	rm -f .coverage
	rm -rf coverage
	rm -rf build
	rm -rf cover
	make -C docs clean
	python setup.py clean
	rm -rf .tox

doc:
	make -C docs html
	@echo "open file://`pwd`/docs/_build/html/index.html"

doc-spelling:
	make -C docs spelling

.PHONY: all build venv flake test vtest testloop cov clean doc