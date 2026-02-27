# Code 2/100
quantity = input("Enter quantity: ") 
price_per_item = 50

# total_cost = quantity * price_per_item
total_cost = int(quantity)* price_per_item


print("Your total cost is: " + str(total_cost))


"""
Q1 . What this code is doing?
Ans: This code is taking input as quantity and add calculate cost by multiply with price per item.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 5th line causes by first line type. The consequences is it print quantity multiple time instead of acutal caculation  causes by both bugs.

Q3. How to solve it?
Ans: To solve it we shoud type cast int to the variable quantity in line one or in line 5 where we multiply it.

"""
