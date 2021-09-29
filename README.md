# A VisiData Cheat Sheet

This repository contains the source files for [A VisiData Cheat Sheet](https://jsvine.github.io/visidata-cheat-sheet/), which provides an abbreviated reference for [VisiData](https://visidata.org/) and is based on [An Introduction to VisiData](https://jsvine.github.io/intro-to-visidata/). It is not meant to be an exhaustive catalog of commands, but rather a concise learning aid for the VisiData-curious.

The cheat sheet is currently available in the following languages:

- [English](https://jsvine.github.io/visidata-cheat-sheet/en/)
- [Spanish](https://jsvine.github.io/visidata-cheat-sheet/es/) (with help from [Data Crítica](https://twitter.com/Datacritica))
- [Italian](https://jsvine.github.io/visidata-cheat-sheet/it/) (by [Associazione onData](https://ondata.it/))
- [German](https://jsvine.github.io/visidata-cheat-sheet/de/) (by [Tobias Dussa](https://github.com/tdussa))

### Other versions

The following versions are based on this repository, but are not directly built through it:

- [Italian A4 duplex version](https://github.com/ondata/guidaVisiData/blob/master/testo/risorse/cheat-sheet_DaStampareFronteRetro_di_GianniVitrano.pdf), by [Gianni Vitrano](https://twitter.com/gbvitrano)

## Creating New Translations

To add a translation, follow these steps:

- Examine this repository's issues, to see whether someone else has begun translating into your language of interest. If they have, please try coordinating with them.

- Create an issue in this repository with the following title: `Translation in progress: {language name}`

- Fork the repository, and create a new branch titled `develop-` + [ISO 639-1 two-letter code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), e.g., `develop-ku` for Kurdish. 

- Add add a corresponding section to the `input/metadata.yaml` file, following the pattern of existing translations. Add your name as an additional author.

- In `input/cheat-sheet.yaml`, add your translations (following the existing examples) of as many section titles, commands, and descriptions as you see fit. If a translation is not provided for any particular part, the built HTML and PDF will use the English phrasing.

- If possible, run the build processs below. Check whether the PDF version fits entirely on one page. If not, attempt to shorten the translations until it does.

## Build Process

For each supported language, there are two build targets: an HTML page, and a one-page PDF. Both can be seen in the `docs/` directory. Building these targets requires the following:

- Python 3
- `pyyaml` and `jinja2` Python libraries 
- Chromium browser (for PDF rendering)
    - On Debian/Ubuntu/etc.: `apt install chromium-browser`

To run the full build: `make clean html; make pdfs`

## Licensing

All code in this repository is available under the [MIT License](https://opensource.org/licenses/MIT). All other text is available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0) license.

## Questions?

Feel free to file an issue or [contact Jeremy](https://www.jsvine.com/).
