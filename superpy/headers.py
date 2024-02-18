from enum import Enum

#header for CSV files / Richtables
class HeaderType(Enum):
    BBOUGHT= ['purchase_id', 'product', 'price', 'quantity', 'expiration_date', 'purchase_date']
    SOLD = ['sold_id', 'bought_id', 'product', 'sell_price', 'quantity', 'sell_date']
    INVENTORY = ['product_id', 'product', 'price', 'purchase_price', 'quanty_bought', 'quantity_sold', 'in_stock', 'expiry_date', 'sale_price', 'expiry_status', 'update_date']
    EXPIRED = ['product_id', 'product', 'expiry_date', 'expired_sold']
    REVENUE = ['period', 'revenue', 'cost']