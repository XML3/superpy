from rich.table import Table
from rich.console import Console
from headers import *

def console_table(header_type):
    #call headers from header file
    if header_type == 'bought':
        headers = bought_header
        
    elif header_type == 'sold':
        headers = sold_header
        
    elif header_type == 'inventory':
        headers = inventory_header
        
    elif header_type == 'expired':
        headers = expired_header
        
    elif header_type == 'revenue':
        headers = revenue_header
        
    else:
        raise ValueError("Invalid header type!")