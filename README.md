# The 1520s Project Website

This repository contains the source files for [The 1520s Project](https://1520s-project.org), an open-access digital library of music from ca. 1510 to ca. 1540.

The site lets users browse, search, analyze, listen to, and download Renaissance scores from The 1520s Project corpus. It serves as the public web interface for project metadata, score discovery, work pages, documentation, and analytical visualizations.

## Project Ecosystem

The website is one part of a larger digital edition infrastructure:

- Public website: `https://1520s-project.org`
- Website repository: `benory/1520s-project-website`
- Score repository: `benory/1520s-project-scores`
- Data server: `https://data.1520s-project.org`

Score files are maintained in the score repository. The data server processes Humdrum files and generates derivative formats and analyses used by the website, including MusicXML, MEI, MIDI, MP3, SVG notation, activity plots, keyscape plots, and playback highlighting data.

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

The top-level `Makefile` refreshes metadata by delegating to `_includes/metadata/Makefile`, which downloads current data from project Google Sheets via Google Apps Script.

Running `make` refreshes `_includes/metadata/assets.json` after the metadata download only when at least seven days have elapsed since the last asset-scan attempt. Otherwise it reuses the existing inventory without contacting GitHub or the data server for asset checks. The tracked `assets-check.json` timestamp preserves this limit across checkouts. This work-ID inventory lists existing downloads, MP3s, timemaps, and both activity and vocal-range plot variants. The generator uses the published scores repository listing for source files and checks data-server response headers for generated assets, rejecting the HTML pages the server returns for missing files. MusicXML uses the repository version when the data-server version is absent.

The asset scan requires Python 3 and curl, checks up to 12 URLs concurrently, and can take several minutes. Network errors, unexpected HTTP errors, or incomplete repository listings fail the update and preserve the previous inventory. Commit `assets.json` and `assets-check.json` with website updates. Failed scans also count toward the seven-day limit. To refresh only assets using the existing work metadata, run `make -C _includes/metadata assets`; top-level `make assets` refreshes metadata first. Both commands respect the same seven-day limit. Work pages use this inventory instead of per-visit availability requests. Assets published after a scan appear after the next refresh and site build.

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
- `Makefile` - metadata refresh command
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

`asset_base_url` selects the project prefix in the shared R2 bucket. The browser tries Cloudflare first, then the existing data server(s) and repository URLs. `cloudflare-assets.json` maps preserved repository/PDF files to their uploaded object keys; it is a snapshot of the verified September 2026 transfer, not a claim of current source revision. Refresh it when publishing a new archive. Known blank JRP PDFs remain blocked. The identical `asset-delivery.js` helpers in both websites implement bounded request timeouts and reject HTML error responses. The bucket needs read-only GET/HEAD CORS for browser score and download requests. Dynamic legacy CGI services remain separate.
