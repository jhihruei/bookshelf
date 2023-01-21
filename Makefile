.PHONY: start-docker
start-docker:
	docker run -it -p 3000:3000 --mount type=bind,source=$(shell pwd)/backend,target=/app,readonly python:3.10.6-buster sh