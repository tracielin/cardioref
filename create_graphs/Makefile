mytag=cardioref

#
.PHONY: help clean webserver typehints flake8 pylint doctest mccabe

help:
	@echo "make help"
	@echo "      this message"
	@echo "==== Targets outside container ===="
	@echo "make docker"
	@echo "      build and run docker"
	@echo "make docker_build"
	@echo "make docker_live"
	@echo "      build and run docker /bin/bash"
	@echo "==== Targets inside container ===="
	@echo "make png"
	@echo "      create PNG using generate_graphviz.py"
	@echo "make clean"
	@echo "      eliminate SVG files"


docker: docker_build docker_live
docker_build:
	docker build -t $(mytag) .

docker_live:
	docker run -it --rm -v`pwd`:/scratch $(mytag) /bin/sh

docker_svg:
	docker run --rm -v`pwd`:/scratch -w:/scratch $(mytag) python3 generate_graphviz.py

clean:
	rm -rf *.png *.dot

png: clean
	python3 generate_graphviz.py
