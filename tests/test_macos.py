"""Test the mdinfo_macos plugin"""

import os

import pytest
from click.testing import CliRunner
from mdinfo.cli import cli

TEST_FILE = "tests/test_files/pears.jpg"

TEST_DATA = {
    "{exiftool:Keywords|sort}": ["fruit pears"],
    "{exiftool:XMP:Title}": ["Pears on a tree"],
}

def test_macos():
    """"Dummy test"""
    assert True

