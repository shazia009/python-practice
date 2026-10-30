# # # # # PRACTICE 1 
# # # # # lamps=2400
# # # # # delivery_Cost=350
# # # # # Order_Lamps=3*lamps
# # # # # EachDelivery_Cost=delivery_Cost*3
# # # # # totalCost=Order_Lamps+EachDelivery_Cost
# # # # # print(totalCost)

# # # # # print(type(totalCost))

# # # # # PRACTICE 2
# # # # # A form gave you the name " aMNA rAZA ". Clean it so it reads Amna Raza (look up the .title() method), then print Welcome, Amna Raza! Your name has 9 characters. using an f-string and len().

# # # # # name="aMNA rAZA"
# # # # # print(f"Welcome {name.title()} your name has {len(name)} characters")

# # # # # Practice 3: a product record

# # # # # Create a list of three prices: [850, 1200, 400]. Print the last price and the sum of all three. Then create a dictionary for one product with the keys name, price and in_stock. Change in_stock to False and print just the product's name.
 
# # # # # prices= [850, 1200, 400]
# # # # # print(prices[2])
# # # # # print(sum(prices ))
# # # # # print(prices)

# # # # # products={"name":" laptop","price":1200,"in_Stock":True}
# # # # # print(products)
# # # # # products["in_Stock" ]=False
# # # # # print(products)
# # # # # print(products["name"])

# # # # # Practice 4: free delivery

# # # # # Create two variables: total = 6200 and city = "Lahore". Print Free delivery if the total is at least Rs 5,000 and the city is Lahore. Otherwise print Delivery charge: Rs 350. Change the values a few times to test both outcomes.
# # # # # total = 6200 
# # # # # city = "Lahore"

# # # # # if city == "Lahore" and total >= 5000:
# # # # #     print("Free delivery!")
# # # # # else:
# # # # #     print("Delivery charge: Rs 350.")
    
    
# # # #   # practice 5
# # # #   # sales tax. An order's subtotal is Rs 7,200 and sales tax is 18%. Print the tax amount and the total with tax (expected: 1296.0 and 8496.0). Print the type of the tax amount. Why is it a float when the subtotal was an int?
 
# # # # # total =7200
# # # # # tax=18
# # # # # saletax=total*tax/100
# # # # # print(saletax)
# # # # # subtotal=saletax+total
# # # # # print(subtotal)
# # # # # print(type(saletax))
 
# # # #   #practice 6 
# # # #   # Splitting a bill. Four friends split a Rs 4,750 dinner. Print each person's share using /. Then look up the // and % operators and use them to print how many whole rupees each person pays and how many rupees are left over.
  
# # # # # total_Rupees=4750
# # # # # total_person=4
# # # # # EachShare=total_Rupees/total_person
# # # # # print(EachShare)
# # # # # whole_Rupees=EachShare//total_person
# # # # # print(whole_Rupees)
# # # # # rupeesleft=total_Rupees%total_person
# # # # # print(rupeesleft)

# # # # # practice 6
# # # #  A phone costs Rs 15,000. Apply a 10% discount, then add 18% tax to the discounted price, and print the final price. Now do it the other way round: tax first, then the discount. Do you get the same answer? Write a comment in your code explaining why or why not.
# # # # phone_cost=15000
# # # # disount=10
# # # # tax=18
# # # # discounted=phone_cost*disount/100
# # # # print(discounted)
# # # # price_after_discount = phone_cost - discounted
# # # # tax_amount = price_after_discount * tax / 100
# # # # finalprice=price_after_discount + tax_amount
# # # # print(finalprice)




# # # # # practice 7
# # # # # Create two variables: total = 6200 and city = "Lahore". Print Free delivery if the total is at least Rs 5,000 and the city is Lahore. Otherwise print Delivery charge: Rs 350.
# # # # TOTAL=6200
# # # # city="Lahore"
# # # # if TOTAL>=500:
# # # #   print("free delivery")
# # # # elif city=="Lahore":
# # # #   print("free delivery")
# # # # else:
# # # #   print("delivery charge:Rs 350")  

# # # # practice 8
# # # A shop is shipping 23 items, and each box holds 6. Using only arithmetic (no if), print the number of full boxes, the number of items left over, and the total number of boxes needed, including a partly full one (expected: 3, 5 and 4). Each box costs Rs 120 to ship: print the shipping cost. Test your code with 24 items. Does the box count still come out right


# # # import math
# # # items = 23
# # # eachbox = 6
# # # box_cost = 120

# # # full_boxes = items // eachbox
# # # leftover_items = items % eachbox


# # # total_boxes =math.ceil (items  / eachbox)
# # # shipping_cost = total_boxes * box_cost

# # # print("--- For 23 Items ---")

# # # print("Full boxes:", full_boxes)
# # # print("Leftover items:", leftover_items)
# # # print("Total boxes needed:", total_boxes)

# # # practice 9   working with text
# # # Clean an email. Clean " Ali.Khan@GMAIL.com " so it has no spaces and is all lowercase, then print Email: ali.khan@gmail.com (18 characters).
# # # name=" Ali.Khan@GMAIL.com "
# # # newname=name.strip().lower()
 
# # # print("Email:",newname,f"({len(newname)} characters)")

# # # practice 10
# # # The item name is " wireless MOUSE ", the price is 2499 and the quantity is 3. Print exactly: Wireless Mouse x3 = Rs 7,497. Work out the total in code; don't type the number.
# # # Itemname="wireless mouse"
# # # price=2499
# # # quantity=3
# # # new=price*quantity
# # # print("wirless mouse*3=",new)

# # # practice 11 
# # # Look up the .replace() and .upper() methods. Turn the raw code " ord-2024-0042 " into ORD20240042, then print Order ORD20240042 has 11 characters. Can you do the whole clean-up in one line by chaining methods

# # # rawcode=" ord-2024-0042 "
# # # newcode=rawcode.replace("-","").upper().strip()
# # # print("Order",newcode,"has",f"{len(newcode)} characters")


# # # practice 12
# # # You have first = " bilal ", last = "QURESHI " and city = "lahore". Look up string slicing (for example text[0:3]). Build the username bilal.qureshi_lah (lowercase first name, a dot, lowercase last name, an underscore and the first three letters of the city), then print:

# # # first="bilal"
# # # last="QURESHI"
# # # city="lahore"
# # # newuser = f"your username is {(u := f'{first.lower()}.{last.lower()}_{city[0:3].lower()}')} {len(u)} characters"
# # # print("Welcome, Bilal Qureshi from Lahore!")
# # # print(newuser)

# # # practice 13     
# # #  Store a shop's daily sales for one week in a list: [18500, 22300, 19800, 25400, 31200, 42800, 38600]. Print Monday's and Sunday's sales, the weekly total and the daily average, formatted as Rs with commas and no decimals. Then look up max() and min() and print the best and worst days' sales.
# # from tkinter.ttk import Notebook


# # dailysale=[18500, 22300, 19800, 25400, 31200, 42800, 38600]
# # monday_sales=dailysale[0]
# # sunday_sales=dailysale[6]
# # weekly_total = sum(dailysale)
# # daily_average = weekly_total // len(dailysale)
# # best_day = max(dailysale)
# # worst_day = min(dailysale)
# # print(f"monday_Sale Rs:{monday_sales}")
# # print(f"sunday_Sale Rs:{sunday_sales}")
# # print(daily_average)
# # print(best_day)
# # print(worst_day)

# # # # practice 14
# # # Create a dictionary of stock counts: {"pens": 120, "notebooks": 45, "staplers": 8}. The shop sells 30 notebooks: update the count by subtracting from the current value, not by typing 15. Add a new product, "markers", with 60 in stock. Print how many products there are (use len()) and then the whole dictionary.
 
# # stockcounts={"pens": 120, "notebooks": 45, "staplers": 8}
# # stockcounts["notebooks"]=stockcounts["notebooks"]-30
# # print(stockcounts)
# # stockcounts ["markers"]=60
# # print(f"Total number of products: {len(stockcounts)}")
# # print(stockcounts)

 
# # #  practice 15
# # #  Create a list of three order dictionaries, each with id, customer and total. Without a loop:

# # # Print the customer of the second order.
# # # The third order gets a Rs 500 discount: change its total.
# # # Add a fourth order to the end of the list.
# # # Print 4 orders. The first is A101 and the last is A104., taking every value from the list.

# # orders = [
# #     {"id": "A101", "customer": "Ali", "total": 4500},
# #     {"id": "A102", "customer": "Bilal", "total": 12800},
# #     {"id": "A103", "customer": "Sana", "total": 2300}
# # ]
 
# # print("second customer:",orders[1]["customer"])

# # orders[2]["total"]=orders[2]["total"]-500
# # orders.append({"id": "A104", "customer": "Zain", "total": 7500})
# # print(f"{len(orders)} orders. The first is {orders[0]['id']} and the last is {orders[-1]['id']}.")


# # # practice 16
# #   #  Build one dictionary for a customer that contains a nested dictionary and a list:
# #   # customer = {
# #   #     "name": "Noor Foods",
# #   #     "address": {"city": "Karachi", "area": "Clifton"},
# #   #     "order_totals": [4500, 12800, 2300],
# #   # }
# #   # Print the customer's city, their number of orders and the total they've spent. Add a new order of Rs 6,100, then print the new total. Finally, try customer["phone"] and read the error you get. Look up the dictionary .get() method and use it to print No phone number instead of crashing.

# # customer = {
# #     "name": "Noor Foods",
# #     "address": {"city": "Karachi", "area": "Clifton"},
# #     "order_totals":[4500, 12800, 2300],
# # }
# # print("city",customer["address"]["city"])
# # print("Number of orders:", len(customer["order_totals"]))
# # print("Total spent: Rs", sum(customer["order_totals"]))
# # customer["order_totals"].append(6100)
# # print("New total spent: Rs", sum(customer["order_totals"]))
# # print(customer.get("phone", "No phone number"))

# # practice 17
# # 1. Formatting rupees. Write a function format_rupees(amount) that returns text such as Rs 12,800. Test it with 12800, 999 and 1250000. Then use it to print Noor Foods owes Rs 11,520


# # def format_rupees(amount):
# #   return f"Rs {amount}"
# # print(format_rupees(12800))
# # print(format_rupees(999))
# # print(format_rupees(1250000))
# # balance_owed = 11520
# # print(f"Noor Foods owes {format_rupees(balance_owed)}")


# # practice 18
# Return or print? Write add_tax(subtotal, rate=0.18). The rate=0.18 part is a default value: it's used when you don't pass a rate. Check that add_tax(7200) returns 8496.0 and add_tax(7200, 0.05) returns 7560.0. Now write a second version that uses print() instead of return, store its result in a variable and print the variable. What do you get, and why?


def add_tax(subtotal, rate=0.18):
  return subtotal + (subtotal * rate)
print(add_tax(7200))
print(add_tax(7200, 0.05))
def add_tax_print(subtotal, rate=0.18):
     print(subtotal + (subtotal * rate))
result = add_tax_print(7200)
print("Stored variable contains:", result)