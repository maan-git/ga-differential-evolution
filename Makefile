
install:
	@echo "--> Installing requirements"
	pip install -r requirements-dev.txt
	@echo "--> Installing black"
	pip install black
	@echo "--> Installing pre-commit"
	pip install pre-commit
	pre-commit install
	@echo ""

lint:
	@echo "--> Running black"
	black --check .
	@echo ""

safety:
	@echo "--> Running safety"
	safety check
	@echo ""

test:
	@echo "--> Running tests"
	pytest  -vv -s --cov-fail-under 10 --cov=./ --cov-report xml:coverage/coverage.xml --cov-report html:coverage/coverage_html --cov-report term-missing .
	@echo ""

clean:
	@echo "--> Removing .pyc and __pycache__"
	find . | grep -E "__pycache__|.pyc$$" | xargs rm -rf
	@echo ""
	@echo "--> Removing coverage data"
	rm -rf .coverage* .cache htmlcov
	rm -rf ./coverage
	rm -rf ./build
	rm -rf ./dist
	@echo ""

lint-fix:
	@echo "--> Auto fix lint errors "
	black .
	@echo ""

run:
	@echo "--> Running"
	sh entrypoint.sh