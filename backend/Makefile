########
# DEV #
######
## [Run command in backend container]
## Usage: make run-cmd cmd="cmd to be run"
run-cmd:
	docker-compose -f docker-compose.dev.yml run --rm warehouse-backend $(cmd)

## [Run unit tests]
## Usage: make unit-tests
test:
	$(MAKE) run-cmd cmd="nosetests"
