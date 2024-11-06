# Here is where we will write our code
from datetime import datetime

class Transaction: 
    """
    Represents import/export transactions
    
    Attributes:
    transaction_ID (str): A unique identifier for each transaction, ensuring easy tracking and reference.
    product (str): The specific product involved in the transaction.
    import_export (str): Indicates whether the transaction is an import or export.
    quantity (int): The amount of the product traded
    value (float): The monetary value of the product in USD.  
    date (str): The date when the transaction occurred. (00-00-000)
    
    methods: parse_date to convert date string to datetime object
    """
    def __init__(self, transaction_ID, product, country, value, date):
        self.transaction_ID = transaction_ID
        self.product = product
        self.country = country
        self.value = value
        self.date = date
        
    def parse_date(date):
        return datetime.strptime(date, "%d-%m-%Y").date()
        

    # data management (nick)
    def load_data(file_path): 
        """
    load import and export data csv file
    
    parameters: 
        file_path (str): path to csv file
        
    returns:
        list (transactions): list of transaction objects
        """ 
    
    def add_transaction(transactions, transaction):
        """
        add new transaction to dataset
    
        parameters: 
        tranasactions (list [transaction]): current transactions list
        transaction (transaction): new transaction 
    
        returns: 
            new transaction list
        """
    def delete_transaction(transactions, transaction_id):
        """
    delete transaction by id
    
        parameters:
            transactions (list[transaction]): current transactions
            transaction_id (str): transaction id to delete
        
        returns: 
            boolean: true if deleted, false otherwise
        """
        
        
        
        
class Product:
    """
    Represents the products
    
    Attributes: 
    customs_code (str): The customs or Harmonized System (HS) code used for product classification.
    category (str): The category of the product, such as Electronics, Clothing, Machinery, etc.

    """
    def __init__ (self, product_name, category, customs_code):
        self.product_name = product_name
        self.category = category
        self.customs_code = customs_code
  

class location:
    """
    Represents the location
    
    Attributes:
    country (str): The name of the country of origin or destination.
    port (str): The port where the product was either shipped from or received.

    """
    def __init__ (self, country_name, port):
        self.country_name = country_name
        self.port = port
    

# Data Management and Storage (Nicholas)
# Description: Load data from the CSV file, handle storage, and provide functions for CRUD (create, read, update, delete) operations on transactions.

# Analytical Functions (Seamus)
# Description: Implement functions for data analysis, such as total trade value calculations, data filtering, and identifying trends based on date or product category.

# User Interaction Module (Garrette)
# Description: Develop the command-line interface for user interactions, including navigation through various functionalities like querying and viewing reports.

# Data Reporting and Summary Generation (John)
# Description: Develop functions that summarize and present key metrics to the user. Create readable outputs in a user-friendly format, based on the analytical functions and data management. 


        
        