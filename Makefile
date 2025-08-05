PYTHON = python

cache: clean
	$(PYTHON) -m csearch.main

clean:
	rm -rf cache.db
