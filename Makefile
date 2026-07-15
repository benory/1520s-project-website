## Download metadata for the 1520s project from the Google Spreadsheet
## for the project's metadata. You need to update the SID variable in
## _includes/metadata/Makefile when the deployment of the Google Apps
## Script has changed.
##
## Type "make" in this directory to download the JSON files for the
## metadata into the _includes/metadata directory.
##

all: download

download:
	(cd _includes/metadata && make download)