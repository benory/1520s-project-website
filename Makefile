# Default: refresh metadata, build changed/missing assets, and verify R2 uploads.
.DEFAULT_GOAL := all
ASSET_TOOL_DIR ?= ../digital-library-build
ASSET_PYTHON ?= $(ASSET_TOOL_DIR)/.venv/bin/python
ASSET_IDS ?=
ASSET_ARGS ?=
WORKFLOW = $(ASSET_PYTHON) "$(ASSET_TOOL_DIR)/tools/website/fast-assets.py" --project 1520s --website "$(CURDIR)" $(if $(ASSET_IDS),--ids "$(ASSET_IDS)")

.PHONY: all assets assets-plan assets-audit download texts
all: assets

assets:
	$(WORKFLOW) $(ASSET_ARGS)

assets-audit:
	$(subst tools/website/fast-assets.py,tools/workflow/run.py,$(WORKFLOW)) --audit $(ASSET_ARGS)

assets-plan:
	$(WORKFLOW) --plan $(ASSET_ARGS)

download:
	$(MAKE) -C _includes/metadata download

texts:
	ruby _includes/metadata/build-text-index.rb
