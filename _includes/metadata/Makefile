# Direct Google Sheets CSV downloads; helper lives in digital-library-build.

LIBRARY_BUILD ?= ../../../digital-library-build
SHEET_PYTHON ?= python3
DOWNLOAD = $(SHEET_PYTHON) "$(LIBRARY_BUILD)/tools/metadata/download.py" --project 1520s --website "$(abspath ../..)"
TABLES = works composers commentary modern_editions statistics Josquin

.PHONY: all download assets refresh-assets $(TABLES)
all: refresh-assets
refresh-assets: download
	$(MAKE) assets
assets:
	python3 build-asset-index.py
download:
	$(DOWNLOAD)
$(TABLES):
	$(DOWNLOAD) --table "$@"
