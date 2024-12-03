import pytest
from datetime import datetime
from imports_exports import ImportExportSystem, Transaction, parse_date

# To run: python -m pytest

@pytest.fixture

# Setup system with transactions
def setup_system():
    transactions = [
        Transaction(transaction_ID="1", country="USA", product="Electronics", value=1000.0, date="01-01-2021"),
        Transaction(transaction_ID="2", country="Canada", product="Electronics", value=1500.0, date="15-01-2021"),
        Transaction(transaction_ID="3", country="USA", product="Furniture", value=2000.0, date="20-01-2021"),
        Transaction(transaction_ID="4", country="Mexico", product="Electronics", value=2500.0, date="25-01-2021"),
        Transaction(transaction_ID="5", country="USA", product="Electronics", value=3000.0, date="30-01-2021")
    ]
    return ImportExportSystem(transactions)

# Test filter transactions by country
def test_filter_transactions_by_country(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(country="USA")
    assert len(filtered_transactions) == 3, f"Expected 3 transactions, but got {len(filtered_transactions)}"

# Test filter transactions by product
def test_filter_transactions_by_product(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(product="Electronics")
    assert len(filtered_transactions) == 4, f"Expected 4 transactions, but got {len(filtered_transactions)}"

# Test filter transactions by date range
def test_filter_transactions_by_date_range(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(date_range=("01-01-2021", "31-01-2021"))
    assert len(filtered_transactions) == 5, f"Expected 5 transactions, but got {len(filtered_transactions)}"

# Test filter transactions by country and product
def test_filter_transactions_by_multiple_criteria(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(country="USA", product="Electronics")
    assert len(filtered_transactions) == 2, f"Expected 2 transactions, but got {len(filtered_transactions)}"

# Test that all transactions are returned when no filters are applied
def test_filter_transactions_empty_filters(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions()
    assert len(filtered_transactions) == len(system.transactions), "Expected all transactions to be returned when no filters are applied."

# Test filter transactions with non-numeric value for min_value
def test_filter_transactions_non_numeric_min_value(setup_system):
    system = setup_system
    with pytest.raises(TypeError) as excinfo:
        system.filter_transactions(min_value="non_numeric_value")
    assert "not supported between instances of 'float' and 'str'" in str(excinfo.value), f"Expected TypeError for non-numeric min_value, but got: {excinfo.value}"

# Test filter transactions with non-numeric value for max_value
def test_filter_transactions_non_numeric_max_value(setup_system):
    system = setup_system
    with pytest.raises(TypeError) as excinfo:
        system.filter_transactions(max_value="non_numeric_value")
    assert "not supported between instances of 'float' and 'str'" in str(excinfo.value), f"Expected TypeError for non-numeric max_value, but got: {excinfo.value}"

# Test filter transactions with negative min_value
def test_filter_transactions_negative_min_value(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(min_value=-1000.0)
    assert len(filtered_transactions) == len(system.transactions), "Expected all transactions to be returned when min_value is negative."

# Test filter transactions with negative max_value
def test_filter_transactions_negative_max_value(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(max_value=-1000.0)
    assert len(filtered_transactions) == 0, "Expected 0 transactions to be returned when max_value is negative."

# Test filter transactions with min_value greater than max_value
def test_filter_transactions_min_value_greater_than_max_value(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(min_value=3000.0, max_value=1000.0)
    assert len(filtered_transactions) == 0, "Expected 0 transactions to be returned when min_value is greater than max_value."

# Test filter transactions with invalid country format (numeric)
def test_filter_transactions_invalid_country_format(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(country="12345")
    assert len(filtered_transactions) == 0, "Expected 0 transactions for invalid country format, but found some transactions."

# Test filter transactions with invalid product format (numeric)
def test_filter_transactions_invalid_product_format(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(product="12345")
    assert len(filtered_transactions) == 0, "Expected 0 transactions for invalid product format, but found some transactions."
 
# Test filter transactions by a non-existent product
def test_filter_transactions_non_existent_product(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(product="NonExistentProduct")
    assert len(filtered_transactions) == 0, "Expected 0 transactions for a non-existent product, but found some transactions."

# Test that no transactions are returned when an empty date range is provided
def test_filter_transactions_empty_date_range(setup_system):
    system = setup_system
    filtered_transactions = system.filter_transactions(date_range=("", ""))
    assert len(filtered_transactions) == 0, "Expected 0 transactions for empty date range, but found transactions."

# Test parse date with invalid date format
def test_parse_date_invalid_format():
    invalid_date = "invalid_date"
    with pytest.raises(ValueError) as excinfo:
        parse_date(invalid_date)
    assert "time data 'invalid_date' does not match format '%d-%m-%Y'" in str(excinfo.value), f"Expected ValueError for invalid date format, but got: {excinfo.value}"

# Test adding a new transaction
def test_add_transaction(setup_system):
    system = setup_system
    system.add_transaction("6", "Brazil", "Coffee", 500.0, "01-02-2021")
    assert len(system.transactions) == 6, "Expected 6 transactions after adding a new one, but found a different number."

# Test updating a transaction 
def test_update_transaction(setup_system):
    system = setup_system
    updated = system.update_transaction("1", country="UK", product="Books", value=1200.0, date="02-01-2021")
    assert updated, "Expected transaction to be updated successfully."
    transaction = system.search_transaction_by_id("1")
    assert transaction.country == "UK", "Expected country to be updated to UK."
    assert transaction.product == "Books", "Expected product to be updated to Books."
    assert transaction.value == 1200.0, "Expected value to be updated to 1200.0."
    assert transaction.date == "02-01-2021", "Expected date to be updated to 02-01-2021."

# Test deleting a transaction
def test_delete_transaction(setup_system):
    system = setup_system
    deleted = system.delete_transaction("1")
    assert deleted, "Expected transaction to be deleted successfully."
    transaction = system.search_transaction_by_id("1")
    assert transaction is None, "Expected transaction to be None after deletion."

# Test searching for a transaction by ID
def test_search_transaction_by_id(setup_system):
    system = setup_system
    transaction = system.search_transaction_by_id("1")
    assert transaction is not None, "Expected to find transaction with ID 1."
    assert transaction.transaction_ID == "1", "Expected transaction ID to be 1."