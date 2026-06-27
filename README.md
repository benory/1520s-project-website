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

## Metadata

Website metadata is stored in `_includes/metadata/` as JSON files. These files support search, filtering, work pages, composer information, modern edition data, and statistical visualizations.

The main metadata files are:

- `works.json` - work-level metadata used throughout the site
- `composers.json` - composer metadata and links
- `modern_editions.json` - information about modern editions
- `statistics.json` - aggregate data for charts and summaries
- `Josquin.json` - Josquin attribution table metadata

The top-level `Makefile` refreshes metadata by delegating to `_includes/metadata/Makefile`, which downloads current data from project Google Sheets via Google Apps Script.

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
