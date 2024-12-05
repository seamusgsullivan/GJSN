""""
This program is an Import/Export Management System that allows users to filter, sort, add, update, delete, search, view summaries, and export transactions to CSV files.
"""

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
        date (datetime): The date the transaction occurred.
    """
    def __init__(self, transaction_ID, product, country, value, date):
        """
        Initializes a Transaction object with the given attributes.
        
        Args:
            transaction_ID (str): The unique identifier for the transaction.
            product (str): The name of the product.
            country (str): The country of origin or destination.
            value (float): The monetary value of the transaction.
            date (datetime): The date the transaction took place.
            
        Side effects:
            Initializes the Transaction object with the given attributes.
        """
        self.transaction_ID = transaction_ID
        self.product = product
        self.country = country
        self.value = value
        self.date = date
        
class ImportExportSystem:
    """
    Manages a list of transactions and provides methods to analyze them.
    
    Attributes:
        transactions (list): A list of Transaction objects.
    """
    def __init__(self, transactions):
        """
        Initializes the ImportExportSystem with a list of transactions.
        
        Args:
            transactions (list): A list of Transaction objects.
            
        Side effects:
            Initializes the ImportExportSystem with the given list of transactions.
        """
        self.transactions = transactions
    
    def total_trade_value(self, transactions):
        """
        Calculates the total value of a list of transactions.
    
        Args:
            transactions (list[Transaction]): The list of transactions to calculate the total value for.
    
        Returns:
            float: The total value of the given transactions.
        """
        total_value = 0
        for t in transactions:
            total_value += t.value
        return total_value

    def filter_transactions(self, date_range=None, country=None, product=None, min_value=None, max_value=None):
        """
        Filters transactions based on the given criteria.
        
        Args:
            date_range (tuple): A tuple containing start and end dates for filtering transactions.
            country (str): The country to filter transactions by.
            product (str): The product to filter transactions by.
            min_value (float): The minimum value for filtering transactions.
            max_value (float): The maximum value for filtering transactions.
            
        Returns:
            list: A list of Transaction objects that meet the filtering criteria.
        """
        filtered_transactions = []
        for t in self.transactions:
            if date_range:
                start_date, end_date = date_range
                if not (start_date <= t.date <= end_date):
                    continue
            if country and t.country.lower() != country.lower():
                continue
            if product and t.product.lower() != product.lower():
                continue
            if min_value and t.value < min_value:
                continue
            if max_value and t.value > max_value:
                continue
            filtered_transactions.append(t)
        return filtered_transactions
    
    def add_transaction(self, transaction_ID, country, product, value, date):
        """
        Adds a new transaction to the list of transactions.
        
        Args:
            transaction_ID (str): The unique identifier for the transaction.
            country (str): The country of origin or destination.
            product (str): The name of the product.
            value (float): The monetary value of the transaction.
            date (datetime): The date the transaction took place.
        """
        transaction = Transaction(transaction_ID, country, product, value, date)
        self.transactions.append(transaction)
    
    def update_transaction(self, transaction_ID, country=None, product=None, value=None, date=None):
        """
        Updates an existing transaction with new information.
        
        Args:
            transaction_ID (str): The unique identifier for the transaction to update.
            country (str): The new country value.
            product (str): The new product value.
            value (float): The new value.
            date (datetime): The new date.
            
        Returns:
            boolean: True if the transaction was updated successfully, False otherwise.
        """
        for t in self.transactions:
            if t.transaction_ID == transaction_ID:
                if country:
                    t.country = country
                if product:
                    t.product = product
                if value:
                    t.value = value
                if date:
                    t.date = date
                return True
        return False
    
    def delete_transaction(self, transaction_ID):
        """
        Deletes a transaction from the list of transactions.
        
        Args:
            transaction_ID (str): The unique identifier for the transaction to delete.
            
        Returns:
            boolean: True if the transaction was deleted successfully, False otherwise.
        """
        for t in self.transactions:
            if t.transaction_ID == transaction_ID:
                self.transactions.remove(t)
                return True
        return False
    
    def search_transaction_by_id(self, transaction_ID):
        """
        Searches for a transaction by its unique identifier.
        
        Args:
            transaction_ID (str): The unique identifier to search for.
            
        Returns:
            Transaction: The Transaction object with the given ID, or None if not found.
        """
        for t in self.transactions:
            if t.transaction_ID == transaction_ID:
                return t
        return None
    
    def sort_transactions_by_value(self, transactions, descending):
        """
        Sorts transactions by value in either ascending or descending order.
        
        Args:
            descending (bool): If True, sort in descending order; otherwise, sort in ascending order.
            
        Returns:
            list: A list of Transaction objects sorted by value.
        """
        return sorted(transactions, key=lambda x: x.value, reverse=descending)
    
    def export_transactions_to_csv(self, transactions, filename):
        """
        Exports transactions to a CSV file.
        
        Args:
            transactions (list[Transaction]): The list of transactions to export.
            filename (str): The name of the file to save the CSV data to.
            
        Side effects:
            Writes transaction data to a CSV file with the given filename.
        """
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Transaction_ID", "Country", "Product", "Value", "Date"])
            for t in transactions:
                writer.writerow([t.transaction_ID, t.country, t.product, t.value, t.date.strftime("%d-%m-%Y")])

    def generate_transaction_summary(self, transactions):
        """
        Generates a summary of the transactions.
        
        Args:
            transactions (list[Transaction]): The list of transactions to generate a summary for.
            
        Returns:
            list: A list containing the total number of transactions, total trade value, and average trade value.
        
        Side effects:
            Calculates the total number of transactions, total trade value, and average trade value. 
        """
        total_transactions = len(transactions)
        total_value = self.total_trade_value(transactions)
        average_value = 0
        if total_transactions:
            average_value = total_value / total_transactions
        summary = [total_transactions, total_value, average_value]
        return summary

def parse_date(date):
    """
    Converts a date string in 'dd-mm-yyyy' format to a datetime object.
        
    Args:
        date (str): The date string to be parsed.
        
    Returns:
        datetime: A datetime object representing the given date.
    """
    return datetime.strptime(date, "%d-%m-%Y")

def load_data(file_path):
    """
    Loads transaction data from a CSV file and returns a list of Transaction objects.
    
    Args:
        file_path (str): The path to the CSV file containing transaction data.
    
    Returns:
        list: A list of Transaction objects loaded from the CSV file.
        
    Side effects:
        Reads data from the CSV file and creates Transaction objects based on the data.
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
                date=parse_date(row[6])
            )
            transactions.append(transaction)
    return transactions










############# new functions 

# get_imports_exports_per_country
# get_unique_countries
# show_country_imports_exports

# get_category_counts
# show_category_counts

# get_total_import_export_counts
# show_highest_import_export

# updated main


def get_imports_exports_per_country(file_path, country_name):
    """
    Calculates the number of imports and exports for a specific country.

    Parameters:
        file_path (str): The path to the CSV file.
        country_name (str): The name of the country to analyze.

    Returns:
        tuple: A tuple containing the count of imports and exports.
    """
    imports = 0
    exports = 0

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Country'].strip().lower() == country_name.strip().lower():
                if row['Import_Export'].strip().lower() == "import":
                    imports += 1
                elif row['Import_Export'].strip().lower() == "export":
                    exports += 1
    return imports, exports


def get_unique_countries(file_path):
    """
    Returns a sorted list of unique countries from the CSV file.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        list: A sorted list of unique country names.
    """
    countries = []  # List to store all countries found in the "Country" column

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['Country']
            countries.append(country)

    unique_countries = set(countries)  # Remove duplicates by converting to a set
    return sorted(unique_countries)


def show_country_imports_exports(file_path):
    """
    Prompts the user to select a country and displays its import/export counts.

    Parameters:
        file_path (str): The path to the CSV file.
    """
    sorted_countries = get_unique_countries(file_path)  # Get the unique countries
    print("\nSelect a country from the list below:")
    for i, country in enumerate(sorted_countries, start=1):
        print(f"{i}. {country}")

    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= choice <= len(sorted_countries):
            selected_country = sorted_countries[choice - 1]
            imports, exports = get_imports_exports_per_country(file_path, selected_country)
            print(f"\n      {selected_country}:")
            print(f"        - Imports: {imports}")
            print(f"        - Exports: {exports}")
        else:
            print("Invalid choice. Please enter a valid number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")


from collections import defaultdict
# Define the possible product categories
PRODUCT_CATEGORIES = ["Clothing", "Electronics", "Furniture", "Machinery", "Toys"]
def get_category_counts(file_path, country_name):
    """
    Returns the count of product categories for a specific country based on imports and exports.

    Parameters:
        file_path (str): The path to the CSV file.
        country_name (str): The name of the country to analyze.

    Returns:
        dict: A dictionary containing category counts for imports and exports.
    """
    import_counts = defaultdict(int)  # Default dict to store import counts per category
    export_counts = defaultdict(int)  # Default dict to store export counts per category

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Country'].strip().lower() == country_name.strip().lower():
                category = row['Category'].strip()  # Get the product category
                if category in PRODUCT_CATEGORIES:  # Ensure the category is one of the defined categories
                    if row['Import_Export'].strip().lower() == "import":
                        import_counts[category] += 1  # Increment the import count for the category
                    elif row['Import_Export'].strip().lower() == "export":
                        export_counts[category] += 1  # Increment the export count for the category

    # Return both the import and export category counts
    return dict(import_counts), dict(export_counts)


def show_category_counts(file_path):
    """
    Prompts the user to select a country and displays the category counts for imports and exports.

    Parameters:
        file_path (str): The path to the CSV file.
    """
    sorted_countries = get_unique_countries(file_path)  # Get the unique countries
    print("\nSelect a country from the list below:")
    for i, country in enumerate(sorted_countries, start=1):
        print(f"{i}. {country}")

    try:
        choice = int(input("\nEnter the number corresponding to your choice: "))
        if 1 <= choice <= len(sorted_countries):
            selected_country = sorted_countries[choice - 1]
            import_counts, export_counts = get_category_counts(file_path, selected_country)

            print(f"\n      {selected_country}:")
            print("          Imports:")
            for category in PRODUCT_CATEGORIES:
                print(f"          - {category}: {import_counts.get(category, 0)}")

            print("\n          Exports:")
            for category in PRODUCT_CATEGORIES:
                print(f"          - {category}: {export_counts.get(category, 0)}")
        else:
            print("Invalid choice. Please enter a valid number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def get_total_import_export_counts(file_path):
    """
    Returns the total import and export counts for each country.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        dict: A dictionary containing total import and export counts for each country.
    """
    country_imports = defaultdict(int)  # Default dict to store total import counts per country
    country_exports = defaultdict(int)  # Default dict to store total export counts per country

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['Country'].strip()
            if row['Import_Export'].strip().lower() == "import":
                country_imports[country] += 1  # Increment the import count for the country
            elif row['Import_Export'].strip().lower() == "export":
                country_exports[country] += 1  # Increment the export count for the country

    # Return both the import and export totals
    return country_imports, country_exports


def show_highest_import_export(file_path):
    """
    Prompts the user to choose whether to view the country with the highest number of imports or exports.

    Parameters:
        file_path (str): The path to the CSV file.
    """
    country_imports, country_exports = get_total_import_export_counts(file_path)

    print("\nChoose an option:")
    print("1. Highest imports")
    print("2. Highest exports")
    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        highest_imports_country = max(country_imports, key=country_imports.get)
        highest_imports_value = country_imports[highest_imports_country]
        print(f"\n     Country with the highest number of imports:\n      - {highest_imports_country}")
        print(f"      - Total imports:  {highest_imports_value}")

    elif choice == "2":
        highest_exports_country = max(country_exports, key=country_exports.get)
        highest_exports_value = country_exports[highest_exports_country]
        print(f"\n     Country with the highest number of exports:\n      - {highest_exports_country}")
        print(f"      - Total exports: {highest_exports_value}")

    else:
        print("Invalid choice. Please enter 1 or 2.")


def main():
    """
    Runs the Import/Export Management System allowing user interaction.
    """
    file_path = 'Imports_Exports_Dataset.csv'
    transactions = load_data(file_path)

    system = ImportExportSystem(transactions)
    filtered_created = False

    while True:
        print("\n--- Import/Export Insights ---")
        print("1. View country with the highest number of imports or exports")
        print("2. View number of imports and exports per country")
        print("3. View all categories for a country's imports and exports") 
        print("\n--- Import/Export Management System ---")
        print("4. Filter transactions")
        print("5. Sort transactions by value")
        print("6. Add a new transaction")
        print("7. Update an existing transaction")
        print("8. Delete a transaction")
        print("9. Search transaction by ID")
        print("10. View transaction summary")
        print("11. Export transactions to CSV")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        # New functionality for Import/Export Insights
        if choice == "1":
            show_highest_import_export(file_path)  # Calls the function to show the country with the highest imports/exports
        elif choice == "2":
            show_country_imports_exports(file_path)  # Calls the function to show imports and exports per country
        elif choice == "3":
            show_category_counts(file_path)  # Calls the function to show category counts for a country's imports and exports
        
        
        
        elif choice == "4":
            print("\nFilter Transactions:")
            start_date = input("Enter start date (dd-mm-yyyy) or press Enter to skip: ")
            end_date = input("Enter end date (dd-mm-yyyy) or press Enter to skip: ")
            country = input("Enter country or press Enter to skip: ")
            product = input("Enter product or press Enter to skip: ")
            min_value = input("Enter minimum value (0 - 10000) or press Enter to skip: ")
            max_value = input("Enter maximum value (0 - 10000) or press Enter to skip: ")

            date_range = None
            if start_date and end_date:
                date_range = (parse_date(start_date), parse_date(end_date))
            if min_value:
                min_value = float(min_value)
            if max_value:
                max_value = float(max_value)
            filtered = system.filter_transactions(date_range, country, product, min_value, max_value)
            if filtered:
                filtered_created = True
                print(f"\nFiltered Transactions ({len(filtered)} results):")
                for t in filtered:
                    print(f"Transaction ID: {t.transaction_ID} | Product: {t.product} | "
                          f"Country: {t.country} | Value: ${t.value} | Date: {t.date.strftime('%d-%m-%Y')}")
            else:
                print("No transactions match the filters.")

        elif choice == "5":
            print("\nSort Transactions by Value:")
            sort_choice = input("Do you want to sort the filtered transactions (f) or all transactions (a)? ").lower()
            if sort_choice == "f" and filtered_created:
                print("\nSort Filtered Transactions by Value:")
                order = input("Enter 'asc' for ascending or 'desc' for descending: ").lower()
                if order == 'desc':
                    sorted_transactions = system.sort_transactions_by_value(filtered, True)
                elif order == 'asc':
                    sorted_transactions = system.sort_transactions_by_value(filtered, False)
                else:
                    print("Invalid choice. Please enter 'asc' or 'desc'.")
                    continue

                print(f"\nSorted Filtered Transactions ({len(sorted_transactions)} results):")
                for t in sorted_transactions:
                    print(f"Transaction ID: {t.transaction_ID} | Product: {t.product} | "
                          f"Country: {t.country} | Value: ${t.value} | Date: {t.date.strftime('%d-%m-%Y')}")
            elif sort_choice == "a":
                print("\nSort All Transactions by Value:")
                order = input("Enter 'asc' for ascending or 'desc' for descending: ").lower()
                if order == 'desc':
                    sorted_transactions = system.sort_transactions_by_value(transactions, descending=True)
                elif order == 'asc':
                    sorted_transactions = system.sort_transactions_by_value(transactions, descending=False)
                else:
                    print("Invalid choice. Please enter 'asc' or 'desc'.")
                    continue
                
                print(f"\nSorted All Transactions ({len(sorted_transactions)} results):")
                for t in sorted_transactions:
                    print(f"Transaction ID: {t.transaction_ID} | Product: {t.product} | "
                          f"Country: {t.country} | Value: ${t.value} | Date: {t.date.strftime('%d-%m-%Y')}")
            else:
                print("Invalid choice. Either the input was not recognized, or you attempted to use a filtered transaction list when none exists.")

        elif choice == "6":
            print("\nAdd a New Transaction:")
            transaction_ID = input("Enter transaction ID: ")
            product = input("Enter product name: ")
            country = input("Enter country: ")
            value = float(input("Enter transaction value: "))
            date_str = input("Enter transaction date (dd-mm-yyyy): ")
            date = parse_date(date_str)
            system.add_transaction(transaction_ID, product, country, value, date)
            print("Transaction added successfully!")

        elif choice == "7":
            print("\nUpdate an Existing Transaction:")
            transaction_ID = input("Enter the transaction ID to update: ")
            product = input("Enter new product name (or press Enter to skip): ")
            country = input("Enter new country (or press Enter to skip): ")
            value = input("Enter new transaction value (or press Enter to skip): ")
            date_str = input("Enter new transaction date (dd-mm-yyyy) (or press Enter to skip): ")
            if date_str:
                date = parse_date(date_str)
            if value:
                value = float(value)
            success = system.update_transaction(transaction_ID, country, product, value, date)
            if success:
                print("Transaction updated successfully!")
            else:
                print("Transaction not found.")

        elif choice == "8":
            print("\nDelete a Transaction:")
            transaction_ID = input("Enter the transaction ID to delete: ")
            success = system.delete_transaction(transaction_ID)
            if success:
                print("Transaction deleted successfully!")
            else:
                print("Transaction not found.")

        elif choice == "9":
            print("\nSearch Transaction by ID:")
            transaction_ID = input("Enter the transaction ID to search for: ")
            transaction = system.search_transaction_by_id(transaction_ID)
            if transaction:
                print(f"Transaction ID: {transaction.transaction_ID} | Product: {transaction.product} | "
                      f"Country: {transaction.country} | Value: ${transaction.value} | Date: {transaction.date.strftime('%d-%m-%Y')}")
            else:
                print("Transaction not found.")

        elif choice == "10":
            print("\nTransaction Summary:")
            summary_choice = input("Do you want a summary of the filtered transactions (f) or all transactions (a)? ").lower()
            if summary_choice == "f" and filtered_created:
                summary = system.generate_transaction_summary(filtered)
                print(f"Total Filtered Transactions: {summary[0]}")
                print(f"Total Filtered Trade Value: ${round(summary[1], 2)}")
                print(f"Average Filtered Trade Value: ${round(summary[2], 2)}")
            elif summary_choice == "a":
                summary = system.generate_transaction_summary(transactions)
                print(f"Total Transactions: {summary[0]}")
                print(f"Total Trade Value: ${round(summary[1], 2)}")
                print(f"Average Trade Value: ${round(summary[2], 2)}")
            else:
                print("Invalid choice. Either the input was not recognized, or you attempted to use a filtered transaction list when none exists.")

        elif choice == "11":
            print("\nExport Transactions to CSV:")
            export_choice = input("Do you want to export the filtered transactions (f) or all transactions (a)? ").lower()
            if export_choice == "f" and filtered_created:
                filename = input("Enter the filename to save as (e.g., 'output.csv'): ")
                system.export_transactions_to_csv(filtered, filename)
                print(f"Filtered transactions exported successfully to {filename}!")
            elif export_choice == "a":
                filename = input("Enter the filename to save as (e.g., 'output.csv'): ")
                system.export_transactions_to_csv(transactions, filename)
                print(f"All transactions exported successfully to {filename}!")
            else:
                print("Invalid choice. Either the input was not recognized, or you attempted to use a filtered transaction list when none exists.")

        elif choice == "12":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()




