## Download metadata for the 1520s project from the Google Spreadsheet
## for the project's metadata. You need to update the SID variable in
## _includes/metadata/Makefile when the deployment of the Google Apps
## Script has changed.
##
## Type "make" in this directory to download the JSON files for the
## metadata into the _includes/metadata directory.
##

.PHONY: all download texts assets

all: assets texts

# Metadata must finish before checking its work IDs, including with make -j.
assets: download
	$(MAKE) -C _includes/metadata assets

download:
	$(MAKE) -C _includes/metadata download

# Refresh the work-ID index from the published scores repository.
texts:
	ruby _includes/metadata/build-text-index.rb
