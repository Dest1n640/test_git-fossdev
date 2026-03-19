.DEFAULT_GOAL := help

help:
	@echo "This makefile for repo-level activity"

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Create directory demo-practive"
	mkdir -p $(PRACTICE)
	cp practiceMakefile $(PRACTICE)/Makefile

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Remove directory demo-practice"
	rm -rf $(PRACTICE)

# mkdir demo-practice
# mkdir demo-practice/src
# mkdir demo-practice/tests
# mkdir demo-practice/docs
# mkdir demo-practice/README.md
