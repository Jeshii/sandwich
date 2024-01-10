#! /usr/bin/env python3

import pickledb
from rich.table import Table
from rich import print

db = pickledb.load('sandwich.json', False)

toppings = db.get('toppings')


table = Table(show_header=True, header_style="bold magenta")
table.add_column("Ingredient")
table.add_column("Quantity", justify="right")
table.add_column("Unit")

for topping in toppings:
    table.add_row(topping['name'],str(topping['quantity']),topping['unit'])

print(table)