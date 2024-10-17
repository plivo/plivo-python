.PHONY: build test run

build:
	docker-compose up --build --remove-orphans

start:
	docker-compose up --build --remove-orphans --detach
	# Wait for the container to be running before attaching
	@while [ -z "$$(docker-compose ps -q pythonSDK)" ]; do \
		sleep 1; \
	done
	docker attach $$(docker-compose ps -q pythonSDK)

test:
	@[ "${CONTAINER}" ] && \
		(docker exec -it $$CONTAINER /bin/bash -c "tox -e py") || \
		(tox -e py)

run:
	@[ "${CONTAINER}" ] && \
		(docker exec -it $$CONTAINER /bin/bash -c "cd /usr/src/app/python-sdk-test/ && python test.py") || \
		(cd /usr/src/app/python-sdk-test/ && python test.py)