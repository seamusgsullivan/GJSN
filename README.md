# Import/Export Management System
INST326 Final Project by Team GJSN

Overview:
The Import/Export Management System is a Python command-line program designed to help users manage, organize, and analyze international trade transactions. The program reads transaction data from a CSV file, processes it, and provides useful insights, such as identifying trends in imports and exports, calculating total values, and categorizing data. The system helps businesses streamline their import/export processes by providing essential data-driven information in an accessible format.

How to Run the Program:
1. Ensure that Python is installed on your system.
2. Download or clone the project repository.
3. Open the terminal or command prompt.
4. Navigate to the project directory containing the Python scripts.
5. Run the program by executing the following command:

python imports_exports.py

This will start the program and process the data from the CSV file. The output will be displayed in the terminal.


How to Use the Program:
After running the program, the user will be prompted with a main menu offering a variety of options to interact with the import/export data. The available choices are as follows:

1. Filter transactions: The user can filter the transactions by any combination of the following:
    - Date: Filter transactions by a specific date range.
    - Country: Filter transactions based on the country of origin or destination.
    - Product: Filter transactions by the product being imported or exported.
    - Value: Filter transactions based on the transaction value.
2. Sort transactions by value: Sort all transactions in ascending or descending order based on their monetary value.
3. Add a new transaction: Allows the user to add a new transaction to the dataset by providing the required details.
4. Update a transaction: Lets the user update an existing transaction by searching for it via its unique transaction ID.
5. Remove a transaction: Enables the user to delete a transaction by providing its transaction ID.
6. Search for a transaction by ID: The user can search for and view a specific transaction using its unique transaction ID.
7. View transaction summary: Provides a summary of a list of transactions, such as total transactions, total trade value, and average trade value.
8. Export transactions to CSV: The user can export a list of transactions to a CSV file for use outside the program.
9. Exit the program: Exits the program and returns control to the command line.

After making a selection, the user will be prompted to enter any necessary information (such as a date range, country, or product), and the program will display the results or take the requested action. Once an action is completed, the user will return to the main menu to select another option or exit the program.

Interpreting the output:
- If the user selects an option to view or filter transactions, the program will display the relevant records in a clean, readable format.
- When sorting or exporting, the program will sort the transactions accordingly or save the data to a CSV file.
- Summary options will present key metrics, such as totals and averages, for the dataset.
- Errors or invalid inputs will prompt the program to ask for valid entries until a correct input is provided.

Dataset source:
https://www.kaggle.com/datasets/chakilamvishwas/imports-exports-15000?resource=download
