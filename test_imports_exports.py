import pytest
from imports_exports import Transaction, ImportExportSystem, load_data

# To run: pytest test_imports_exports.py

@pytest.fixture
def setup_system():
    """Loads the system and transactions for each test."""
    file_path = 'Imports_Exports_Dataset.csv'
    transactions = load_data(file_path)
    system = ImportExportSystem(transactions)
    return system

def test_invalid_country(setup_system):
    """Test filtering by an invalid country name."""
    system = setup_system
    invalid_country = "Atlantis"  # Country doesn't exist
    transactions = system.filter_by_country(invalid_country)
    assert len(transactions) == 0, f"Expected 0 transactions for invalid country '{invalid_country}', but found {len(transactions)}."

def test_empty_country_name(setup_system):
    """Test filtering by an empty country name."""
    system = setup_system
    empty_country = ""  # Edge case: empty string
    transactions = system.filter_by_country(empty_country)
    assert len(transactions) == 0, "Expected 0 transactions for empty country name, but found transactions."

def test_invalid_product_name(setup_system):
    """Test filtering by an invalid product name."""
    system = setup_system
    invalid_product = "Unicorn Horns"  # Product doesn't exist
    transactions = system.filter_by_product(invalid_product)
    assert len(transactions) == 0, f"Expected 0 transactions for invalid product '{invalid_product}', but found {len(transactions)}."

def test_invalid_operator(setup_system):
    """Test filtering by value with an invalid operator."""
    system = setup_system
    value = 10000
    invalid_operator = "less or equal to"  # Invalid operator
    transactions = system.filter_by_value(value, invalid_operator)
    assert len(transactions) == 0, f"Expected 0 transactions for invalid operator '{invalid_operator}', but found {len(transactions)}."

def test_empty_operator(setup_system):
    """Test filtering by value with an empty operator string."""
    system = setup_system
    value = 10000
    empty_operator = ""  # Edge case: empty operator
    transactions = system.filter_by_value(value, empty_operator)
    assert len(transactions) == 0, "Expected 0 transactions for empty operator, but found transactions."

def test_invalid_date_format(setup_system):
    """Test filtering by an invalid date format."""
    system = setup_system
    start_date = "01-13-2023"  # Invalid date (13th month)
    end_date = "31-12-2023"
    with pytest.raises(ValueError) as excinfo:
        system.filter_by_date_range(start_date, end_date)
    assert "time data" in str(excinfo.value), f"Expected ValueError for invalid date format, but got: {excinfo.value}"

def test_start_date_after_end_date(setup_system):
    """Test filtering with a start date that comes after the end date."""
    system = setup_system
    start_date = "31-12-2023"
    end_date = "01-01-2023"
    transactions = system.filter_by_date_range(start_date, end_date)
    assert len(transactions) == 0, f"Expected 0 transactions for invalid date range '{start_date} to {end_date}', but found {len(transactions)}."

def test_large_numeric_value(setup_system):
    """Test filtering by an unusually large value."""
    system = setup_system
    large_value = 10000000  # Very large trade value
    operator = "greater than"
    transactions = system.filter_by_value(large_value, operator)
    assert len(transactions) == 0, f"Expected 0 transactions for value greater than {large_value}, but found {len(transactions)}."
    
def test_invalid_date_format_letters(setup_system):
    """Test filtering by a date with random letters (invalid format)."""
    system = setup_system
    start_date = "abcdefgh"  # Invalid date format (random letters)
    end_date = "2023-12-31"
    with pytest.raises(ValueError) as excinfo:
        system.filter_by_date_range(start_date, end_date)
    assert "time data" in str(excinfo.value), f"Expected ValueError for invalid date format, but got: {excinfo.value}"

def test_invalid_value_format_letters(setup_system):
    """Test filtering by a value with random letters (invalid format)."""
    system = setup_system
    invalid_value = "abc123"  # Invalid value format (letters and numbers)
    operator = "greater than"
    with pytest.raises(TypeError) as excinfo:
        system.filter_by_value(invalid_value, operator)
    assert "not supported between instances of 'float' and 'str'" in str(excinfo.value), f"Expected TypeError for invalid value format, but got: {excinfo.value}"