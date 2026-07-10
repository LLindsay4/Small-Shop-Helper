#-------------------- List of imports --------------------
import csv                                  # To read data from the spreadsheet the Small Shop provided
import os                                   # To handle file paths
from datetime import datetime, timezone     # Work with dates, times, and timezones

#-------------------- Variables --------------------
my_list = []    # An empty list to store all products loaded from spreadsheet
cart = []       # An empty list to store items added by the user
total = 0.0     # Running total of the cart
now = datetime.now()

#-------------------- Access to Spreadsheet --------------------
abs_dir = os.path.dirname(os.path.abspath(__file__))        # Get the absolute path of the current folder
product_file = "//products.csv"                             # Path to the spreadsheet containing product information                                 

#-------------------- Load product data from CSV --------------------
with open(abs_dir + product_file, newline="") as file:      # Open the spreadsheet file
    reader = csv.DictReader(file)                           # Read spreadsheet rows as dictionaries (more organised and easier to read!)
    for row in reader:                                      # Loop through each row
        my_list.append(row)                                 # Add each product to the product list

#-------------------- Menu Loop --------------------
while True:     # A conditional loop for the menu; that will run indefinitely until the user chooses to exit
    print('''
--- MAIN MENU ---
Press 'p' to view the product list
Press 'i' to view the inventory
Press ENTER to add a new item
Press 'q' to exit the program
''')

    choice = input("Select an option: ").lower()                                # Get user input and convert to lowercase
    
    #-------------------- Product list option --------------------
    if choice == 'p':
        print("\n--- PRODUCT LIST ---")
        for product in my_list:                                                 # Loop through products
            print(product["Product_ID"], product["Product_Description"])        # Show product ID and product description

    #-------------------- Inventory option --------------------
    elif choice == 'i':
        print("\n--- INVENTORY ---")
        for product in my_list:                                                 # Loop through products
            print(
                product["Product_ID"],                                          # Show stock product ID
                product["Product_Description"],                                 # Show stock product description
                product["Amount_In_Stock"]                                      # Show stock amount
            )

    #-------------------- Quit option --------------------
    elif choice == 'q':
            print()
            print("===== INVOICE =====")
            # Print all items in the cart with their prices first
            for item, price in cart:
                print(f"{item:<30} £{price:<0.2f}")                            #print with a format of 30 width and 2 decimal points

            print("----------------------------------------")

            # Keep outside loop to print subtotal once, do not place under discount or it will be applied to subtotal AND final total
            print(f"{'Subtotal':<30} £{total:>0.2f}") 

            # Apply discount if subtotal is greater than or equal to 30
            if total >= 30:
                discount = total * 0.10
                total = total - discount
                print(f"{'10% Discount applied:':<30} £{discount:>0.2f}")
  
            # Print final total
            print(f"{'Final total':<30} £{total:>0.2f}")
            print("----------------------------------------")
            print("Thank you for your patronage. Have a nice day.")
            print("----------------------------------------")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))                        # Formatted time
            print()
            break        

    #-------------------- Add item to cart --------------------
    elif choice == '':                                                      # ENTER key pressed
        product_id = input("Enter Product ID: ")                            # User enters Product ID

        for product in my_list:                                             # Loop through all products
            if product["Product_ID"] == product_id:                         # Check for a match
                price = float(product["Cost"])                              # Get price as a float
                cart.append((product["Product_Description"], price))        # Add a tuple (name, price) to cart. A tuple in this case counts as one argument
                total = total + price                                       # Add price to total
                print(product["Product_Description"], "added. £", price, "charged.")
                break
        else:                                                               # Runs if no break occurred and user has entered an ID not found in the spreadsheet
            print("Invalid Product ID. Please try again.")              

    #-------------------- Invalid menu option --------------------
    else:
        print("Invalid option. Please try again.")                          # Runs if input is not 'p', 'i', ENTER, or 'q'



