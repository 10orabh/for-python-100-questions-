# Code 3/100
item_price = 1500.50
discount_percentage = 15.0

# Discount calculate kar rahe hain
discount_amount = item_price * (discount_percentage / 100)
final_price = item_price - discount_amount

print("The final discounted price is: " + str(final_price))


"""
Q1 . What this code is doing?
Ans: This code is calculating final price by removing discounted price from item price.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 6th line causes by second line discounted percentage type which is string and also the when we fix first bug there is another bug in print function because of we can't concate the float and string. The consequences is typeerror.

Q3. How to solve it?
Ans: To solve it we should remove the string and assign  float value to the variable quantity in line one or in line 5 where we multiply it.

"""
