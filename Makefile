.PHONY: clean html pdfs
CHROMIUM ?= chromium-browser

clean:
	rm -r docs
	mkdir docs docs/downloads
	echo "<html><head><meta http-equiv='refresh' content='0; url=./en/' /></head></html>" > docs/index.html

html:
	pipenv run python scripts/build.py

pdfs: $(patsubst \
	docs/%/index.html, \
	docs/downloads/visidata-cheat-sheet.%.pdf, \
	$(wildcard docs/*/index.html) \
)

docs/downloads/visidata-cheat-sheet.%.pdf: docs/%/index.html
	$(CHROMIUM) \
		--headless \
		--disable-gpu \
		--no-margins \
		--print-to-pdf="$@" $< 
