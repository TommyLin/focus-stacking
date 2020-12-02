
WORKING_DIR = $(shell pwd)

.DEFAULT_GOAL = lint
.PHONY: lint clean


lint:
	sudo docker run -e RUN_LOCAL=true -v $(WORKING_DIR):/tmp/lint github/super-linter

clean:
	@rm -rfv super-linter.log
