#! /usr/bin/env python3

import pickledb

# create database or use existing one
db = pickledb.load('sandwich.json', False)

# set some values
db.set('toppings', [
                    {'name': 'lettuce', 'quantity': 1, 'unit': 'heads'}, 
                    {'name': 'tomato', 'quantity': 0, 'unit': 'each'}, 
                    {'name': 'onion', 'quantity': 2, 'unit': 'each'},
                    {'name': 'american cheese', 'quantity': 10, 'unit': 'slices'},
                    ])
db.set('condiments', [
                    {'name': 'mayo', 'quantity': 20, 'unit': "ml"}, 
                    {'name': 'mustard', 'quantity': 25, 'unit': "ml"}, 
                    {'name': 'relish', 'quantity': 15, 'unit': "g"},
                    ])
db.set('breads', [
                    {'name': 'nogami', 'quantity': 2, 'unit': 'slices'}, 
                    {'name': 'banana', 'quantity': 2, 'unit': 'slices'},
                    ])

db.dump()