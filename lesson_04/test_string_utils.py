import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

# Тесты для capitalize()
def test_capitalize_positive(utils):
    result = utils.capitalize("skypro")
    assert result == "Skypro"

def test_capitalize_negative_empty_input(utils):
    with pytest.raises(AttributeError):
        utils.capitalize("")

# Тесты для trim()
def test_trim_positive(utils):
    result = utils.trim("   skypro")
    assert result == "skypro"

def test_trim_negative_empty_input(utils):
    result = utils.trim("")
    assert result == ""

# Тесты для contains()
def test_contains_positive(utils):
    result = utils.contains("SkyPro", "S")
    assert result is True

def test_contains_negative(utils):
    result = utils.contains("SkyPro", "X")
    assert result is False

# Тесты для delete_symbol()
def test_delete_symbol_positive(utils):
    result = utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"

def test_delete_symbol_negative_invalid_input(utils):
    result = utils.delete_symbol("", "k")
    assert result == ""
