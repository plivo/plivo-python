.PHONY: build test run

build:
	docker-compose up --build --remove-orphans

test:
	@[ "${CONTAINER}" ] && \
		(docker exec -it $$CONTAINER /bin/bash -c "tox -e py") || \
		(tox -e py)

run:
	@[ "${CONTAINER}" ] && \
		(docker exec -it $$CONTAINER /bin/bash -c "cd /usr/src/app/python-sdk-test/ && python test.py") || \
		(cd /usr/src/app/python-sdk-test/ && python test.py)