# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:00:15 2017
Fantasy Game Inventory


@author: david.antonini
"""


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# def displayInventory(inventory):
#    total_items = 0
#    for item in inventory:
#        print(str(inventory[item])+' '+item)
#        total_items += inventory[item]
#    print("Total number of items: "+str(total_items))
# This worked but I like the following better:

def displayInventory(inventory):
    total_items = 0
    for item, quantity in inventory.items():
        print(str(quantity)+' '+item)
        total_items += quantity
    print("Total number of items: "+str(total_items))


displayInventory(stuff)


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        # adds a zero valued key to the inventory dict if none exists
        inventory[item] += 1
        # increases value by one, for each appearance in loot list
    return inventory

inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
