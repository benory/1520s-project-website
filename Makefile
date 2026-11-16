# Default: refresh assets, then synchronize the musical search service.
.DEFAULT_GOAL := all
ASSET_TOOL_DIR ?= ../digital-library-build
ASSET_PYTHON ?= $(ASSET_TOOL_DIR)/.venv/bin/python
ASSET_IDS ?=
ASSET_ARGS ?=
SEARCH_WORKFLOW = $(ASSET_PYTHON) "$(CURDIR)/_scripts/update-search-service.py" --toolkit "$(ASSET_TOOL_DIR)"
WORKFLOW = $(ASSET_PYTHON) "$(ASSET_TOOL_DIR)/tools/website/fast-assets.py" --project 1520s --website "$(CURDIR)" $(if $(ASSET_IDS),--ids "$(ASSET_IDS)")

.PHONY: all assets assets-plan assets-audit download texts search search-update search-plan
all: assets
	$(if $(strip $(ASSET_ARGS) $(ASSET_IDS)),@echo "Partial/special asset run: skipping search deployment.",$(MAKE) search-update)

assets:
	$(WORKFLOW) $(ASSET_ARGS)

assets-audit:
	$(subst tools/website/fast-assets.py,tools/workflow/run.py,$(WORKFLOW)) --audit $(ASSET_ARGS)

assets-plan:
	$(WORKFLOW) --plan $(ASSET_ARGS)

search: search-update

search-update:
	$(SEARCH_WORKFLOW)

search-plan:
	$(SEARCH_WORKFLOW) --plan

download:
	$(MAKE) -C _includes/metadata download

texts:
	ruby _includes/metadata/build-text-index.rb
