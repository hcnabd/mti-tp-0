# Part 1: 
prod_cod = input("Enter the product code (e.g., ELEC-001): ")
prod_name = input("Enter the product name (e.g., Keyboard): ")
unit_price = float(input("Enter the unit price (e.g., 445.99): "))
prod_quantity = int(input("Enter the quantity ordered: "))
prod_stock = input("Enter the current stock (e.g., 120): ")
tax_rate = int(input("Enter the tax rate (e.g., 7 for 7%): "))

# Part 2:
prod_stock = float(prod_stock)

# Part 3:
tax_rate = float(tax_rate) / 100  

# Part 4:
subtotal = prod_quantity * unit_price

# Part 5:
tax_amount = subtotal * tax_rate

# Part 6:
total_cost = subtotal + tax_amount

# Part 7:
remaining_stock = prod_stock - prod_quantity

# Part 8:
print("******************************* ORDER RECEIPT *******************************")
print(f"Item Code: {prod_cod}")
print(f"Item Name: {prod_name}")
print(f"Price/Unit: {unit_price:.2f} DA")
print(f"Quantity: {prod_quantity}")
print(f"Subtotal: {subtotal:.2f} DA")
print(f"Tax ({tax_rate * 100:.2f}%): {tax_amount:.2f} DA")
print(f"******************** Total Cost: {total_cost:.2f} DA")
print(f"******************** Remaining Stock: {int(remaining_stock)}")
print("***************************************************************************")

