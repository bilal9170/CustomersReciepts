# Lovely Loveseat
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

lovely_loveseat_price = 254.00

# Stylish Settee
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_settee_price = 180.00

# Luxurious lamp
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = 52.15

# Calculations

# sales tax for business 
sales_tax = .088

# customers total before items scanned
customer_one_total = 0

# item description set to an empty string
customer_one_itemization = ""

# total of customers first item  
customer_one_total = lovely_loveseat_price 

# description of the first item purchased
customer_one_itemization += lovely_loveseat_description

# basket is updated with the second item 
customer_one_total += luxurious_lamp_price

# description of the second item purchased

# adding new line after the first item desc
customer_one_itemization += "\n" "\n"

customer_one_itemization +=  luxurious_lamp_description

# calculating the tax for the customer by multiplying the total amount by the sales tax
customer_one_tax = customer_one_total * sales_tax

# adding the sales tax calculated to the total price  
customer_one_total += customer_one_tax

# *** printing customers reciept ***

# the item description 
print("Customer one items:")
print(customer_one_itemization, "\n")

# the total price 
print("Customer One Total: ", customer_one_total) 