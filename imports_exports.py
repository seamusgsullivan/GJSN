import csv
from datetime import datetime

class Transaction:
    """
    Represents import/export transactions.
    
    Attributes:
        transaction_ID (str): A unique identifier for each transaction.
        product (str): The specific product involved in the transaction.
        country (str): The country of origin or destination.
        value (float): The monetary value of the product in USD.
        date (str): The date the transaction occurred.
    """
    def __init__(self, transaction_ID, product, country, value, date):
        """
        Initializes a Transaction object with the given attributes.
        
        Parameters:
            transaction_ID (str): The unique identifier for the transaction.
            product (str): The name of the product.
            country (str): The country of origin or destination.
            value (float): The monetary value of the transaction.
            date (str): The date the transaction took place.
        """
        self.transaction_ID = transaction_ID
        self.product = product
        self.country = country
        self.value = value
        self.date = date
        
    def parse_date(date):
        """
        Converts a date string in 'dd-mm-yyyy' format to a datetime object.
        
        Parameters:
            date (str): The date string to be parsed.
        
        Returns:
            datetime: A datetime object representing the given date.
        """
        return datetime.strptime(date, "%d-%m-%Y").date()

class ImportExportSystem:
    """
    Manages a list of transactions and provides methods to analyze them.
    
    Attributes:
        transactions (list): A list of Transaction objects.
    """
    def __init__(self, transactions):
        """
        Initializes the ImportExportSystem with a list of transactions.
        
        Parameters:
            transactions (list): A list of Transaction objects.
        """
        self.transactions = transactions

    def total_trade_value(self):
        """
        Calculates the total trade value of all transactions.
        
        Returns:
            float: The total value of all transactions combined.
        """
        total_value = 0
        for t in self.transactions:
            total_value += t.value
        return total_value

    def transactions_by_date_range(self, start_date, end_date):
        """
        Filters transactions by a given date range.
        
        Parameters:
            start_date (str): The start date in 'dd-mm-yyyy' format.
            end_date (str): The end date in 'dd-mm-yyyy' format.
        
        Returns:
            list: A list of transactions that fall within the specified date range.
        """
        start = Transaction.parse_date(start_date)
        end = Transaction.parse_date(end_date)
        filtered_transactions = []
        for t in self.transactions:
            if start <= Transaction.parse_date(t.date) <= end:
                filtered_transactions.append(t)
        return filtered_transactions
    
    def filtered_total_value_by_date_range(self, start_date, end_date):
        """
        Calculates the total value of transactions within the given date range.
    
        Parameters:
            start_date (str): The start date (inclusive) in the format 'dd-mm-yyyy'.
            end_date (str): The end date (inclusive) in the format 'dd-mm-yyyy'.
    
        Returns:
            float: The total value of transactions within the specified date range.
        """
        
        start = Transaction.parse_date(start_date)
        end = Transaction.parse_date(end_date)
        total_value = 0
        for transaction in self.transactions:
            if start <= Transaction.parse_date(transaction.date) <= end:
                total_value += transaction.value
        return total_value

    def filtered_total_value(self, filter_by=None, value=None):
        """
        Calculates the total value of transactions filtered by a specific attribute.

        Parameters:
            filter_by (str): The attribute to filter transactions by (e.g., 'country', 'product').
            value (str): The value to match for filtering (e.g., 'Colombia' for filter_by='country').

        Returns:
            float: The total value of transactions matching the filter.
        """
        filtered_transactions = self.transactions

        if filter_by == 'product' and value:
            filtered_transactions = self.filter_by_product(filtered_transactions, value)
        elif filter_by == 'country' and value:
            filtered_transactions = self.filter_by_country(filtered_transactions, value)
        
        total_value = 0
        for t in filtered_transactions:
            total_value += t.value
        return total_value

    def filter_by_product(self, transactions, product_name):
        """
        Filters transactions by a specific product.

        Parameters:
            transactions (list[Transaction]): The list of transactions to filter.
            product_name (str): The product to filter by.
        
        Returns:
            list[Transaction]: A list of transactions involving the specified product.
        """
        filtered_transactions = []
        for t in transactions:
            if t.product == product_name:
                filtered_transactions.append(t)
        return filtered_transactions
    
    def filter_by_country(self, transactions, country_name):
        """
        Filters transactions by a specific country.
    
        Parameters:
            transactions (list[Transaction]): The list of transactions.
            country_name (str): The country to filter by.
    
        Returns:
            list[Transaction]: A list of transactions involving the specified country.
        """
        filtered_transactions = []
        for t in transactions:
            if t.country == country_name:
                filtered_transactions.append(t)
        return filtered_transactions

def load_data(file_path):
    """
    Loads transaction data from a CSV file and returns a list of Transaction objects.
    
    Parameters:
        file_path (str): The path to the CSV file containing transaction data.
    
    Returns:
        list: A list of Transaction objects loaded from the CSV file.
    """
    transactions = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            transaction = Transaction(
                transaction_ID=row[0],
                product=row[2],
                country=row[1],
                value=float(row[5]),
                date=row[6]
            )
            transactions.append(transaction)
    return transactions

def run_unit_tests():
    """
    Runs the basic unit tests for the ImportExportSystem.
    These tests verify basic functionality.
    """
    print("\nRunning unit tests...")

    # Test 1: Check total trade value
    file_path = 'Imports_Exports_Dataset.csv'
    transactions = load_data(file_path)
    
    system = ImportExportSystem(transactions)
    total_value = system.total_trade_value()
    if round(total_value, 2) == 75493966.8: # Comparing the rounded total_value to the expected value
        print("Test 1 (Total trade value): Passed!")
    else:
        print("Test 1 (Total trade value): Failed!")

    # Test 2: Check transactions by date range
    start_date = "01-01-2023"
    end_date = "31-12-2023"
    transactions = system.transactions_by_date_range(start_date, end_date)
    if transactions:
        print(f"Test 2 (Transactions by date range): Passed! Found {len(transactions)} transaction(s).")
    else:
        print("Test 2 (Transactions by date range): Failed!")

    # Test 3: Check report value generation (example with 'country' filter)
    report_value = system.filtered_total_value("country", "Colombia")
    if report_value >= 0:
        print("Test 3 (Generate report by country): Passed!")
    else:
        print("Test 3 (Generate report by country): Failed!")

    # Test 4: Check filtering by product
    product_transactions = system.filter_by_product(system.transactions, "agency")
    if product_transactions:
        print(f"Test 4 (Filter by product): Passed! Found {len(product_transactions)} transaction(s).")
    else:
        print("Test 4 (Filter by product): Failed!")
        
    # Test 5: Check filtered transactions by country
    country_transactions = system.filter_by_country(system.transactions, "Italy")
    if country_transactions:
        print(f"Test 5 (Filter by country): Passed! Found {len(country_transactions)} transaction(s).")
    else:
        print("Test 5 (Filter by country): Failed!")
    
    # Test 6: Check report value generation for date range
    report_value = system.filtered_total_value_by_date_range("23-09-2022", "12-03-2023")
    if report_value >= 0:
        print("Test 6 (Generate report by date range): Passed!")
    else:
        print("Test 6 (Generate report by date range): Failed!")
        
    print("\nUnit tests completed.")

def main():
    """
    Runs the Import/Export Management System allowing user interaction.
    """
    file_path = 'Imports_Exports_Dataset.csv'
    transactions = load_data(file_path)

    system = ImportExportSystem(transactions)

    while True:
        print("\nImport/Export Management System")
        print("1. View total trade value")
        print("2. View transactions by date range (01-01-2020 - 31-12-2023)")
        print("3. View transactions by country")
        print("4. View transactions by product")
        print("5. Run unit tests")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            total_value = system.total_trade_value()
            print(f"Total trade value: ${round(total_value, 2)}")
        
        elif choice == "2":
            start_date = input("Enter the start date (dd-mm-yyyy): ")
            end_date = input("Enter the end date (dd-mm-yyyy): ")
            total_value = system.filtered_total_value_by_date_range(start_date, end_date)
            transactions = system.transactions_by_date_range(start_date, end_date)
            if transactions:
                print(f"Transactions between {start_date} and {end_date}:")
                for t in transactions:
                    print(f"Transaction_ID: {t.transaction_ID} - Product: {t.product} - Value: {t.value} - Date: {t.date}")
                print(f"Total transactions: {len(transactions)}")
                print(f"Total trade value for transactions in this date range: ${round(total_value, 2)}")
                
            else:
                print(f"No transactions found in this date range.") 

        elif choice == "3":
            country = input("Enter the country to filter transactions by: ")
            transactions = system.filter_by_country(system.transactions, country)
            total_value = system.filtered_total_value("country", country)
            if transactions:
                print(f"Transactions for {country}:")
                for t in transactions:
                    print(f"Transaction_ID: {t.transaction_ID} - Product: {t.product} - Value: {t.value} - Date: {t.date}")
                print(f"Total transactions: {len(transactions)}")
                print(f"Total trade value for transactions from {country}: ${round(total_value, 2)}")
            else:
                print(f"No transactions found for {country}.")
                
        elif choice == "4":
            product_name = input("Enter the product to filter transactions by: ")
            transactions = system.filter_by_product(system.transactions, product_name)
            total_value = system.filtered_total_value("product", product_name)
            if transactions:
                print(f"Transactions for {product_name}:")
                for t in transactions:
                    print(f"Transaction_ID: {t.transaction_ID} - Country: {t.country} - Value: {t.value} - Date: {t.date}")
                print(f"Total transactions: {len(transactions)}")
                print(f"Total trade value for transactions involving {product_name}: ${round(total_value, 2)}")
            else:
                print(f"No transactions found for {product_name}.")
        
        elif choice == "5":
            run_unit_tests()
                
        elif choice == "6":
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()