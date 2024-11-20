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

    def filter_by_date_range(self, start_date, end_date):
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
    
    def filter_by_product(self, product_name):
        """
        Filters transactions by a specific product.

        Parameters:
            transactions (list[Transaction]): The list of transactions to filter.
            product_name (str): The product to filter by.
        
        Returns:
            list[Transaction]: A list of transactions involving the specified product.
        """
        filtered_transactions = []
        for t in self.transactions:
            if t.product == product_name:
                filtered_transactions.append(t)
        return filtered_transactions
    
    def filter_by_country(self, country_name):
        """
        Filters transactions by a specific country.
    
        Parameters:
            transactions (list[Transaction]): The list of transactions.
            country_name (str): The country to filter by.
    
        Returns:
            list[Transaction]: A list of transactions involving the specified country.
        """
        filtered_transactions = []
        for t in self.transactions:
            if t.country == country_name:
                filtered_transactions.append(t)
        return filtered_transactions
    
    def filter_by_value(self, value, operator):
        """
        Filters transactions by a specific value and operator.
        
        Parameters:
            value (float): The value to filter by.
            operator (str): The operator to use for comparison ('greater than', 'less than', 'equal to').
            
        Returns:
            list[Transaction]: A list of transactions that meet the specified criteria.
        """
        filtered_transactions = []
        for t in self.transactions:
            if operator == 'greater than':
                if t.value > value:
                    filtered_transactions.append(t)
            elif operator == 'less than':
                if t.value < value:
                    filtered_transactions.append(t)
            elif operator == 'equal to':
                if t.value == value:
                    filtered_transactions.append(t)
        return filtered_transactions
    
    def filtered_total_value(self, filtered_transactions):
        """
        Calculates the total value of a filtered list of transactions.
    
        Parameters:
            filtered_transactions (list[Transaction]): The list of filtered transactions to calculate the total value for.
    
        Returns:
            float: The total value of the given transactions.
        """
        total_value = 0
        for t in filtered_transactions:
            total_value += t.value
        return total_value

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
        print("5. View transactions by value (0 - 10000)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            total_value = system.total_trade_value()
            print(f"Total trade value: ${round(total_value, 2)}")
        
        elif choice == "2":
            start_date = input("Enter the start date (dd-mm-yyyy): ")
            end_date = input("Enter the end date (dd-mm-yyyy): ")
            transactions = system.filter_by_date_range(start_date, end_date)
            total_value = system.filtered_total_value(transactions)
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
            total_value = system.filtered_total_value(transactions)
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
            total_value = system.filtered_total_value(transactions)
            if transactions:
                print(f"Transactions for {product_name}:")
                for t in transactions:
                    print(f"Transaction_ID: {t.transaction_ID} - Country: {t.country} - Value: {t.value} - Date: {t.date}")
                print(f"Total transactions: {len(transactions)}")
                print(f"Total trade value for transactions involving {product_name}: ${round(total_value, 2)}")
            else:
                print(f"No transactions found for {product_name}.")
                
        elif choice == "5":
            value = float(input("Enter the value to filter transactions by: "))
            operator = input("Enter the operator ('greater than', 'less than', 'equal to'): ")
            transactions = system.filter_by_value(value, operator)
            total_value = system.filtered_total_value(transactions)
            if transactions:
                print(f"Transactions with a value {operator} {value}:")
                for t in transactions:
                    print(f"Transaction_ID: {t.transaction_ID} - Product: {t.product} - Country: {t.country} -  Value: {t.value} - Date: {t.date}")
                print(f"Total transactions: {len(transactions)}")
                print(f"Total trade value for transactions with a value {operator} ${value}: ${round(total_value, 2)}")
            else:
                print(f"No transactions found with a value {operator} {value}.")
        
        elif choice == "6":
            print("Exiting program...")
            break
    
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()