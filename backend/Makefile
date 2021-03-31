########
# DEV #
######
## [Run command in backend container]
## Usage: make run-cmd cmd="cmd to be run"
build-base:
	docker build -f docker/development/base/Dockerfile -t warehouse-backend-base .

run-cmd:
	docker-compose -f docker-compose.test.yml run --rm warehouse-backend $(cmd)

## [Run unit tests]
## Usage: make unit-tests
test:
	$(MAKE) run-cmd cmd="nosetests"

lint:
	$(MAKE) run-cmd cmd="flake8 --config=setup.cfg --max-complexity=12 $(PYFILES)"
