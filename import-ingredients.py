#! /usr/bin/env python3

import pickledb

# create database or use existing one
db = pickledb.load('sandwich.json', False)

# set some values
db.set('toppings', [
                    {'name': 'lettuce', 'quantity': 1, 'unit': 'heads'}, 
                    {'name': 'tomato', 'quantity': 0, 'unit': 'each'}, 
                    {'name': 'onion', 'quantity': 2, 'unit': 'each'},
                    ])
db.set('cheese', [
                    {'name': 'american', 'quantity': 10, 'unit': 'slices'}, 
                    {'name': 'mozzarella', 'quantity': 500, 'unit': 'g'}, 
                    {'name': 'provalone', 'quantity': 0, 'unit': 'each'},
                    {'name': 'cottage', 'quantity': 0, 'unit': 'g'},
                    ])
db.set('meat', [
                    {'name': 'bacon', 'quantity': 1, 'unit': 'slices'}, 
                    {'name': 'pastrami', 'quantity': 0, 'unit': 'g'}, 
                    {'name': 'ham', 'quantity': 0, 'unit': 'each'},
                    {'name': 'chicken can', 'quantity': 0, 'unit': 'g'},
                    {'name': 'tuna can', 'quantity': 0, 'unit': 'g'},
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