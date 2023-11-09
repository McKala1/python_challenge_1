# McKala's Menu dictionary
menu = {
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
            "Smoked Jackfruit Roll": 24.57
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
my_list = []
order_list = []

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
    if menu_category == "q":
        print("Thank you come again!")
        break 
    if menu_category == "Q":
        print("Thank you come again!")
        break 
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
            item = input("What is the menu item that you want to order?")
            
            # 3. Check if the customer typed a number
            import re
            # user_input = input("Enter a number: ")
            if (menu_category.isdigit):
                print("Awesome! We will be right out with that!")
            else:
                print("Input is not a number.")
            # Convert the menu selection to an integer
            integer_value = int(item)
        
                 # 4. Check if the menu selection is in the menu items

            if integer_value in menu_items:
                print("Item is in the menu.")
            else:
                print("Item is not in the menu, please re-start program.")

                     # Store the item name as a variable
            item_name = menu_items[integer_value]["Item name"]
            item_price = menu_items[integer_value]["Price"]

                     # Ask the customer for the quantity of the menu item
    item_amount = input(f"How many {item_name}('s) would you like to order? ")

                     # Check if the quantity is a number, default to 1 if not    
    try: 
        quantity = int(item_amount)
        if quantity <= 0:
            print("Invalid quantity. Defaulting to 1.")
            quantity = 1
    except:
        print("Invalid quantity. Defaulting to 1.")
        quantity = 1


                    # Add the item name, price, and quantity to the order list
    menu_items[integer_value]['Price']
    item_details = {
                 "item_name": item_name,
                 "item_price": item_price,
                 "quantity": quantity
                              }
    order_list.append(item_details)
    print(f"You ordered {quantity} {item_name} for ${item_price*quantity}. Enjoy your {item_name}!")

                    # Tell the customer that their input isn't valid

                # Tell the customer they didn't select a menu option


            # Tell the customer they didn't select a menu option

        # Tell the customer they didn't select a number

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop
        
                # Complete the order
        match keep_ordering.lower():
            # Customer chose yes
                case 'y':
                # Keep ordering
                    place_order = True
                # Exit the keep ordering question loop
                    break
            # Customer chose no
                case 'n':
                # Complete the order
                    place_order = False
                # Since the customer decided to stop ordering, thank them for their order
                    print("Thank you for your order.")
                # Exit the keep ordering question loop
                    break


    print(f"You ordered {item_name} for ${item_price}. Enjoy your {item_name}!")


                # Since the customer decided to stop ordering, thank them for
                # their order
    print("Thank you so much for ordering with us! ")

                # Exit the keep ordering question loop
if menu_category == 'q':


                # Tell the customer to try again
                print("I did not quite understand that. Please try again.")


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
total_cost = 0
# 6. Loop through the items in the customer's order
for menu_index in range(len(order_list)):
  
    # 7. Store the dictionary items as variables
    item_name = order_list[menu_index]["item_name"]
    item_price = order_list[menu_index]["item_price"]
    quantity = order_list[menu_index]["quantity"]
    total_cost += item_price * quantity

    # 8. Calculate the number of spaces for formatted printing
    my_variable_item_name = 29- len(item_name)
    my_variable_price = 11- len(str(item_price)) 

    # 9. Create space strings
    item_spaces = " " * my_variable_item_name
    price_spaces = " " * my_variable_price

    # 10. Print the item name, price, and quantity
    print(f'{item_name}{item_spaces}{item_price}{price_spaces}{quantity}')    

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
# Initialize an empty order list to store the items
print(f'Here is your total cost: ${total_cost}')