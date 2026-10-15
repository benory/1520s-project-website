# The 1520s Project Website

This repository contains the source files for [The 1520s Project](https://1520s-project.org), an open-access digital library of music from ca. 1510 to ca. 1540.

The site lets users browse, search, analyze, listen to, and download Renaissance scores from The 1520s Project corpus. It serves as the public web interface for project metadata, score discovery, work pages, documentation, and analytical visualizations.

## Project Ecosystem

The website is one part of a larger digital edition infrastructure:

- Public website: `https://1520s-project.org`
- Website repository: `benory/1520s-project-website`
- Score repository: `benory/1520s-project-scores`
- Generated assets: `https://assets.1520s-project.org/1520s`

Score files are maintained in the score repository. The shared `digital-library-build` tools generate PDFs, MEI, MusicXML, MIDI, MP3, incipits, vocal-range and activity plots, and playback timemaps from Humdrum scores. Published assets are stored in Cloudflare R2.

Work texts are maintained as UTF-8 `.txt` files under `texts/` in the score repository, named with the matching metadata ID, for example `texts/Fva/Fva3002-Adieu_solas.txt`. That directory contains only the edited texts. Running `make` in this website repository refreshes `_includes/metadata/texts.json` from the scores repository's published `main` branch using Ruby and curl. The generator rejects malformed filenames, duplicate IDs, and incomplete listings, preserving the existing index on failure. Commit the updated index with website changes when adding, renaming, or removing texts; `make texts` refreshes just this index.

Work pages include the generated index and fetch the matching text directly from the scores repository. Edits to an existing text require no index rebuild and appear after GitHub's cache refreshes. Text appears beneath Genre, preserving line and stanza breaks; texts longer than three file lines have a See more / See less control. Missing texts leave no empty field. No spreadsheet column or scores-repository script or GitHub Action is required.

## Metadata

Website metadata is stored in `_includes/metadata/` as JSON files. These files support search, filtering, work pages, composer information, modern edition data, and statistical visualizations.

The main metadata files are:

- `works.json` - work-level metadata used throughout the site
- `composers.json` - composer metadata and links
- `modern_editions.json` - information about modern editions
- `statistics.json` - aggregate data for charts and summaries
- `Josquin.json` - Josquin attribution table metadata

Metadata is downloaded directly from Google Sheets as CSV and validated before
updating the local JSON snapshots. The download tools live in the separate
`digital-library-build` toolkit; Google Apps Script is not required. Unchanged
metadata retains its existing contents and timestamps, including the date shown
for the Josquin attribution dataset.

Running `make` checks metadata and local scores for changes, generates and uploads
changed or missing assets to Cloudflare R2, and updates the affected download
records. An unchanged successful run skips asset generation and remote asset
checks. Individual failures are reported and remain queued for retry while other
pieces continue. Commit and push the website changes to publish updated links.

- `make download` refreshes metadata only.
- `make assets-plan` shows the proposed asset work without generating or uploading.
- `make assets-audit` performs a full remote asset check.
- `make texts` refreshes the work-text index only.

## Repository Structure

- `_config.yml` - Jekyll site configuration
- `_includes/` - shared Liquid includes, metadata, scripts, and styles
- `_layouts/` - page templates
- `index.markdown` - home page
- `about/` - project description, people, support, collaborations, and acknowledgments
- `documentation/` - editorial and technical documentation
- `repertoire/` - searchable repertoire page
- `recently_added/` - recently added works page
- `work/` - individual work page template and notation tools
- `Josquin/` - Josquin attribution table page and data
- `images/` - logos, banners, icons, examples, mensuration signs, and headshots
- `Makefile` - metadata and incremental asset workflow
- `CNAME` - GitHub Pages custom domain

## Site Organization

Most top-level pages are directories containing an `index.markdown` file, with page-specific `styles-local.html`, `scripts-local.html`, and/or `scripts-listeners.html` files where needed.

Shared styling and scripts live in `_includes/`, while page templates live in `_layouts/`.

## Technologies

The site uses:

- Jekyll and Liquid
- GitHub Pages
- Vega-Lite for charts
- Verovio and the Humdrum Notation Plugin for notation rendering
- JSON metadata generated from project spreadsheets

## License

See `LICENSE`.

### Cloudflare asset delivery

The website serves generated files from `https://assets.1520s-project.org/1520s`.
The local asset inventory controls which downloads appear on work pages.
`cloudflare-assets.json` records asset routing and publication holds. Browser
requests use read-only access; upload credentials are kept outside this repository.
