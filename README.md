# mdinfo-macos

Plugin for [mdinfo](https://github.com/RhetTbull/mdinfo) that provides access to macOS specific metadata.

## Synopsis

```bash
$ mdinfo -p "{exiftool:XMP:Title}" -p "{exiftool:Keywords}" *.jpeg
flowers.jpeg: Zinia flowers in a field
pears.jpeg: Pears on a tree fruit pears
```

## Installation

Requires [mdinfo](https://github.com/RhetTbull/mdinfo) to be installed.

```bash
pip install mdinfo
pip install mdinfo-exiftool
```

## Template Help

<!-- [[[cog
import cog
from mdinfo_macos import get_markdown_help 
cog.out(
    "\n{}\n".format(get_markdown_help())
)
]]] -->

**MacOS Specific Metadata**
| Field | Description              |
| ----- | ------------------------ |
| {mac} | Format: '{mac:SUBFIELD}' |


The `{mac}` template provides access to a wide range of macOS specific metadata fields
including all Spotlight metadata fields. 

The following attributes are supported:


**Finder Metadata**
| Field | Description                                                          |
| ---- | -------------------------------------------------------------------- |
| {finder} | Get metadata managed by macOS Finder such as tags and comments; use in form '{finder:SUBFIELD}', e.g. '{finder:tags}' |


`{finder}` provides access to Finder metadata; available only on macOS. It must be used in the form `{finder:SUBFIELD}` 
where SUBFIELD is one of the following:

| Subfield | Description            |
| -------- | ---------------------- |
| tags     | Finder tags (keywords) |
| comment  | Finder comment         |


<!-- [[[end]]] -->

## Testing

Tested on Ubuntu Linux and macOS Ventura using Python 3.9, 3.10, and 3.11.

## Contributing

Contributions of all kinds welcome. Please see [README_DEV.md](README_DEV.md) for more notes on the development environment and tooling.
