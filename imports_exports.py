# Here is where we will write our code

class Transaction: 
    """ 
    represents trade transaction
    
    attributes: 
        transaction_id (str): transaction identifier
        product (product): product
        country (country): country
        value (float): cost of transaction
        date (date): date of transaction
    """
    
    def __init__(self, transaction_id, product, country, value, date):
        """
        initialize transaction
        
        parameters: 
            transaction_id (str): transaction_id
            product: product
            country: country
            value (float): value
            date: date
        """

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