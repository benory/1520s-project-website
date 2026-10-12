# Direct Google Sheets CSV downloads; helper lives in digital-library-build.
# These legacy IDs are retained only for the earlier standalone comparison pilot.
SID = AKfycbzPjKo_5RlBSDPoHM8vWdw93fisuU6RcKCPpl7cT18qLY7Tx-qhXKxwONcznwbshA-ZmA
SID2 = AKfycbyg7jch405kNehIY8d1fTirMm0BSZgeHXDHoK913A9MjKmMFqIaKBMGN1mphdh_EUArpQ

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
