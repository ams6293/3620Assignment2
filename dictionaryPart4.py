products = {
    "Pencils": "$2.00",
    "Notebook": "$5.00",
    "Laptop": "$700.00",
    "Backpack": "$30.00",
    "Earbuds": "$75.00"
}

print(" Pencils: \n Notebook: \n Laptop \n Backpack \n Earbuds \n")
item = input("Enter the product you would like to see the price of: ")

print(products[item])