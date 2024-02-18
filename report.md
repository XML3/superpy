#Superpy Report

##Supermarket Inventory Management Tool

**Superpy** is a command-line application that manages a supermarket's inventory and its revenue.

This command-line application was build with the use of Python, CSV, Argparse and Richtable.

###CSV File Reading and Writing
**CSV** stands for, command separeted values, and it is the common import and export format for spreadsheets and database.  This is were all append data for this application, like inventory, bought, sold, and sold-expired products, will be found.

Read more...

[CSV Documentation](https://docs.python.org/3/library/csv.html)

###Argparser Parser for command-line options, arguments and sub-commands
The **argparse** module's support for command-line interfaces is build around an instance of `argparse.ArgumentPaser`.  It is a container for argument specifications and has opetions that apply to the parser as whole.

Read more...

[Argparser Documentation](https://docs.python.org/3/library/argparse.html)

###Richtable
**Rich** is a Python library for rich text and beautiful formatting in the terminal.

The Rich API makes it easy to add color and style to terminal output. Rich can also render pretty tables, progress bars, markdown, syntax highlighted source code, tracebacks, and more — out of the box.

Read more...

[Richtable Documentation](https://github.com/textualize/rich/blob/master/README.md)

##Features
The application holds the following features:

* Records new inventory data into CSV file
* Retrieves inventory by created date
* Retrieves products by ID
* Updates inventory data by existing product ID
* Retrieve all expired products
* Checks if expired products were sold, if so, prints these to the CSV file
* Calculates stock based on bought and sold items
* Calculates revenue and cost
* Retrieves revenue profits: using inputs such as yesterday, today, year-month, or specific period of time.


##How to Use **Command line**

**Bought Items**

* Adds new bought products to CSV file, generates new ID:

```
python main.py buy [product, price, quantity, expiration_date(str), purchase_date(str)]
```

**Sold Items**

* Adds sold items to CSV file, It uses `bought ID` in order to sell an existing product, and it generates a new `sold/Sell ID` 

```
python main.py sell [bought_id, product, sell_price, quantity, sell_date(YYYY-MM-DD)(str)]
```


**Inventory**

* Retrieves all inventory data:

```
python main.py inventory
```

* Retrives inventory by specific date (created date) [YYYY-MM-DD]

```
python main.py inventory --date 2024-02-16
```

**Inventory ID**
* Retrieves a product by its ID (use existing product's ID):

```
python main.py inventory_id [product_id]
```

**Add Inventory**

* Add product to inventory:

```
python main.py add_inventory [product, price, purchase_price, quantity_bought, quantity_sold, in_stock, expiry_date, sale_price, expiry_status, created_date]
```

**Inventory Update**

* Products can be updated in the inventory CSV file by using an existing product's id. (Notice the extra command for sale_price) 

```
python main.py update_inventory [product_id] 6 10 5 --sale_price 3.45
```


**Revenue**

* Get today's revenue:

```
python main.py revenue today
```

* Get yesterday's revenue:

```
python main.py yesterday
```

	
* Get revenue by date (Year - Month):

```
python main.py revenue --date [YYYY-MM]
```

* Get revenue for a specific period of time:

```
python main.py revenue --start_date '2023-01-01' --end_date '2024-01-01'
```


**Expire_dates**

* Retrives all expired products based on expiry_dates inside inventory, if so it will print these items to the CSV file

```
python main.py expire_dates --all
```
