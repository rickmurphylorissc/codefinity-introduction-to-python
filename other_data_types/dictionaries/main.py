grocery_inventory = {
    "Milk": (113, "Dairy"), 
    "Eggs": (116, "Dairy"), 
    "Bread": (117, "Bakery"), 
    "Apples": (141, "Produce")
}

bread_details = grocery_inventory.get("Bread")
print(bread_details)