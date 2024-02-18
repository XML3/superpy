from rich.table import Table
from rich.console import Console
from headers import HeaderType

def create_table(header_type: HeaderType):
    headers = header_type.value
    print("Headers:", headers)
    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    print("Table created sucessfully")
    for header in headers:
        table.add_column(header)

    return console, table

def add_row(table: Table, *data):
    table.add_row(*data)