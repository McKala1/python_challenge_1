# McKala's Menu dictionary
Menu = {
    "Appetizers": {
        "Butternut Squash soup": 8.99,
        "Caprese salad": 10.50,
        "Falafel": 9.49,
        "Bruschetta": 7.50
    },
    "Entrees": {
        "Walnut Mushroom Meatloaf": 18.49,
        "Vodka Sauce Lentil Pasta": 24.50,
        "Three Bean Chili": 14.99,
        "Roasted Vegetables": 15.48,
        "Pizza": {
            "Cashew Cheese": 12.50,
            "Margarita": 14.50,
            "Jackfruit BBQ": 16.54
        },
        "Sushi": {
            "Cucumber Roll": 17.50,
            "Smoked Jackfruit Roll" 24.57
        }
    },
    "Drinks": {
        "Mocktails": {
            "Pinapple Express": 8.77,
            "Dirty Russian": 4.59,
            "Tropical Dream": 7.65
        },
        "Water": {
            "Cucumber": 3.99,
            "Lemon": 2.99,
            "Orange": 3.45
        },
        "Tea": {
            "Earl Grey": 5.75,
            "Masala Chia": 6.54,
            "Peppermint": 4.99
        }
    },
    "Dessert": {
        "Strawberry Sorbet": 7.88,
        "Halva": {
            "Vanilla": 5.99,
            "Pistachio": 6.99
        },
        "Peanut Butter brownie": 10.57,
        "Cashew Cookie bar": 11.68,
        "Marshmellow Fluff cookie": 9.50 
    }
} 

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
menu_list = [
    "Appetizers": {
        "Butternut Squash soup": 8.99,
        "Caprese salad": 10.50,
        "Falafel": 9.49,
        "Bruschetta": 7.50
    },
    "Entrees": {
        "Walnut Mushroom Meatloaf": 18.49,
        "Vodka Sauce Lentil Pasta": 24.50,
        "Three Bean Chili": 14.99,
        "Roasted Vegetables": 15.48,
        "Pizza": {
            "Cashew Cheese": 12.50,
            "Margarita": 14.50,
            "Jackfruit BBQ": 16.54
        },
        "Sushi": {
            "Cucumber Roll": 17.50,
            "Smoked Jackfruit Roll" 24.57
        }
    },
    "Drinks": {
        "Mocktails": {
            "Pinapple Express": 8.77,
            "Dirty Russian": 4.59,
            "Tropical Dream": 7.65
        },
        "Water": {
            "Cucumber": 3.99,
            "Lemon": 2.99,
            "Orange": 3.45
        },
        "Tea": {
            "Earl Grey": 5.75,
            "Masala Chia": 6.54,
            "Peppermint": 4.99
        }
    },
    "Dessert": {
        "Strawberry Sorbet": 7.88,
        "Halva": {
            "Vanilla": 5.99,
            "Pistachio": 6.99
        },
        "Peanut Butter brownie": 10.57,
        "Cashew Cookie bar": 11.68,
        "Marshmellow Fluff cookie": 9.50 
    }
]

# Launch the store and present a greeting to the customer
print("Welcome to the McKala's Fancy Palace.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

     # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
                item = input("What is the menu item that you want to order? ")

            # 3. Check if the customer typed a number
                import re
                user_input = input("Enter a number: ")
                if re.match(r'^-?\d+(\.\d+)?$', user_input):
                    print("Input is a number.")
                else:
                    print("Input is not a number.")
                # Convert the menu selection to an integer
                item = "user_input"
                integer_value = int(menu_item)

                # 4. Check if the menu selection is in the menu items
                    menu = [menu_list]
                    item_selection = input("Enter your item selection: ")

                    if item_selection in menu:
                        print("Item is in the menu.")
                    else:
                        print("Item is not in the menu.")

                    # Store the item name as a variable
                    item_name = "user_input"
                    item_price = "user_input"
                    print(f"You ordered {item_name} for ${item_price}. Enjoy your {item_name}!")

                    # Ask the customer for the quantity of the menu item
menu = {menu_list}
print("Menu:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

# Ask the customer for their menu item choice
item_name = input("Enter the name of the item you want to order: ")

# Check if the item is in the menu
if item_name in menu:
    # Ask the customer for the quantity
    quantity = int(input(f"How many {item_name}(s) do you want to order? "))
    
    if quantity > 0:
        # Calculate the total cost
        total_cost = menu[item_name] * quantity
        print(f"You ordered {quantity} {item_name}(s) for a total cost of ${total_cost:.2f}.")
    else:
        print("Invalid quantity. Please enter a positive number.")
else:
    print("Item not found in the menu. Please choose an item from the menu.")

                    # Check if the quantity is a number, default to 1 if not
 quantity_input = input(f"How many {item_name}(s) do you want to order? ")
    
    try:
        quantity = int(quantity_input)
        if quantity <= 0:
            print("Invalid quantity. Defaulting to 1.")
            quantity = 1
    except ValueError:
        print("Invalid input. Defaulting to 1.")
        quantity = 1

    # Calculate the total cost
    total_cost = menu[item_name] * quantity
    print(f"You ordered {quantity} {item_name}(s) for a total cost of ${total_cost:.2f}.")
else:
    print("Item not found in the menu. Please choose an item from the menu.")

                    # Add the item name, price, and quantity to the order list
                        menu_items[item_num]['Price']
                            item_details = {
                              "item_name": item_name,
                              "item_price": menu[item_name],
                              "quantity": quantity
                              }
                               order_list.append(item_details)

                    # Tell the customer that their input isn't valid
                    print("The input is not valid.")

                # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
    menu_category = input("Type menu number to view or q to quit: ")
                # Keep ordering

                # Exit the keep ordering question loop
                if menu_category == 'q':
                     break
                # Complete the order
                complete_order(order)

                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you so much for ordering with us! ")

                # Exit the keep ordering question loop
                 if menu_category == 'q':
                      break

                # Tell the customer to try again
                print("I did not quite understand that. Please try again.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for menu_index in range(len(menu_list)):
    menu_count = menu_purchases[menu_index]
    menu_name = menu_list[menu_index]
    # 7. Store the dictionary items as variables
item_name = order["item_name"]
item_price = order["item_price"]
quantity = order["quantity"]
total_cost = order["total_cost"]

    # 8. Calculate the number of spaces for formatted printing
if alignment == 'left':
    formatted_text = content + ' ' * num_spaces
elif alignment == 'right':
    formatted_text = ' ' * num_spaces + content
elif alignment == 'center':
    formatted_text = ' ' * num_spaces + content + ' ' * num_spaces

print(formatted_text)

    # 9. Create space strings
    num_spaces = 24
    spaces = f"{' ':<{num_spaces}}"

    # 10. Print the item name, price, and quantity
     print(" Here is the menu information" str(item_name) + str(item_quantity) + " is " + str(type(item_quantity)))
    print(f"Item: {item_name}")
    print(f"Price: ${item_price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
# Initialize an empty order list to store the items
order_list = []

# Display the menu to the customer
menu = {menu_list}

print("Menu:")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

while True:
    # Ask the customer for their menu item choice
    item_name = input("Enter the name of the item you want to order (or type 'done' to complete the order): ")

    if item_name.lower() == 'done':
        break

    # Check if the item is in the menu
    if item_name in menu:
        # Ask the customer for the quantity
        quantity_input = input(f"How many {item_name}(s) do you want to order? ")

        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("Invalid quantity. Defaulting to 1.")
                quantity = 1
        except ValueError:
            print("Invalid input. Defaulting to 1.")
            quantity = 1

        # Create a dictionary for the item and add it to the order list
        item_details = {
            "item_name": item_name,
            "item_price": menu[item_name],
            "quantity": quantity
        }
        order_list.append(item_details)
    else:
        print("Item not found in the menu. Please choose an item from the menu.")

# Calculate the cost of the order using list comprehension
order_total = sum(item["item_price"] * item["quantity"] for item in order_list)

# Display the completed order and the total cost
print("Order Details:")
for item in order_list:
    print(f"Item: {item['item_name']}")
    print(f"Price: ${item['item_price']:.2f}")
    print(f"Quantity: {item['quantity']}")
    total_cost = item["item_price"] * item["quantity"]
    print(f"Total Cost: ${total_cost:.2f}")

print(f"Total Order Cost: ${order_total:.2f}")