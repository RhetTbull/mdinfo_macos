"""exiftool template plugin for autofile"""

from __future__ import annotations

import datetime
from typing import Iterable

import mdinfo
import osxmetadata
from osxmetadata import (
    MDIMPORTER_ATTRIBUTE_DATA,
    MDITEM_ATTRIBUTE_DATA,
    NSURL_RESOURCE_KEY_DATA,
    _kFinderColor,
    _kFinderInfo,
    _kFinderStationeryPad,
    _kMDItemUserTags,
)

ALL_ATTRIBUTES = {
    *list(MDITEM_ATTRIBUTE_DATA.keys()),
    *list(NSURL_RESOURCE_KEY_DATA.keys()),
    *list(MDIMPORTER_ATTRIBUTE_DATA.keys()),
    _kFinderColor,
    _kFinderInfo,
    _kFinderStationeryPad,
    _kMDItemUserTags,
}

FIELDS = {"{mac}": "Format: '{mac:SUBFIELD}'"}

DATETIME_ATTRIBUTES = {
    "date": "ISO date, e.g. 2020-03-22",
    "year": "4-digit year, e.g. 2021",
    "yy": "2-digit year, e.g. 21",
    "month": "Month name as locale's full name, e.g. December",
    "mon": "Month as locale's abbreviated name, e.g. Dec",
    "mm": "2-digit month, e.g. 12",
    "dd": "2-digit day of the month, e.g. 22",
    "dow": "Day of the week as locale's full name, e.g. Tuesday",
    "doy": "Julian day of year starting from 001",
    "hour": "2-digit hour, e.g. 10",
    "min": "2-digit minute, e.g. 15",
    "sec": "2-digit second, e.g. 30",
    "strftime": "Apply strftime template to date/time. Should be used in form "
    + "{created.strftime,TEMPLATE} where TEMPLATE is a valid strftime template, e.g. "
    + "{created.strftime,%Y-%U} would result in year-week number of year: '2020-23'. "
    + "If used with no template will return null value. "
    + "See https://strftime.org/ for help on strftime templates.",
}

DATETIME_SUBFIELDS = list(DATETIME_ATTRIBUTES.keys())


@mdinfo.hookimpl
def get_template_help() -> Iterable:
    """Specify help text for your plugin; will get displayed with mdinfo --help
    Returns:
        Iterable (e.g. list) of help text as str or list of lists
        str items may be formatted with markdown
        list of lists items can be used for definition lists (e.g. [[key1, value1], [key2, value2]])
    """

    text = """
    The `{mac}` template provides access to a wide range of macOS specific metadata fields
    including all Spotlight metadata fields. 

    The following attributes are supported:

    """

    text += ", ".join(sorted(ALL_ATTRIBUTES))
    text += "\n"

    fields = [["Field", "Description"], *[[k, v] for k, v in FIELDS.items()]]
    # attributes = [
    #     ["Attribute", "Description"],
    #     *[[k, v] for k, v in DATETIME_ATTRIBUTES.items()],
    # ]
    # return ["**MacOS Specific Metadata**", fields, text, attributes]
    return ["**MacOS Specific Metadata**", fields, text]


@mdinfo.hookimpl
def get_template_value(
    filepath: str, field: str, subfield: str, default: list[str]
) -> list[str | None] | None:
    """Lookup value for {mac} template field.

    Args:
        filepath: path to the file being processed
        field: template field to find value for
        subfield: the subfield provided, if any (e.g. {field:subfield})
        field_arg: the field argument provided, if any (e.g. {field(arg)})
        default: the default value provided to the template, if any (e.g. {field,default})

    Returns:
        The matching template value (which may be None) as a list or None if template field is not handled.

    Raises:
        ValueError: if the template is not correctly formatted (e.g. plugin expected a subfield but none provided)
    """
    if "{" + field + "}" not in FIELDS:
        return None

    if subfield not in ALL_ATTRIBUTES:
        raise ValueError(f"Invalid subfield '{subfield}' for {field} template")

    metadata = osxmetadata.OSXMetaData(filepath)
    value = metadata.get(subfield)
    if not isinstance(value, list):
        value = [value]
    value = [str(v) for v in value]
    return value
