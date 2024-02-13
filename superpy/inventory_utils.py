import csv


#Load inventory data to be used across different function calls
def load_inventory():
    inventory = []
    with open('inventory.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
            inventory.append(row)
    return inventory