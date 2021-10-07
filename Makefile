.PHONY: clean html pdfs
CHROMIUM ?= chromium-browser
SIZES = letter A4

clean:
	rm -r docs
	mkdir docs docs/downloads
	echo "<html><head><meta http-equiv='refresh' content='0; url=./en/' /></head></html>" > docs/index.html

html:
	python scripts/build.py

pdfs: $(foreach size, $(SIZES), $(patsubst \
	docs/%/index.html, \
	docs/downloads/visidata-cheat-sheet.%.$(size).pdf, \
	$(wildcard docs/*/index.html) \
))

docs/downloads/visidata-cheat-sheet.%.pdf:
	$(eval lang = $(word 1, $(subst ., ,$*)))
	$(eval size = $(word 2, $(subst ., ,$*)))
	sed -e "s/size: [^;]*; \/\*◊\*\//size: $(size);/" < docs/$(lang)/index.html > tmp.html
	$(CHROMIUM) \
		--headless \
		--disable-gpu \
		--no-margins \
		--print-to-pdf="$@" tmp.html
	rm tmp.html
