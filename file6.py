# Code 6/50
number = 14

# Checking if the number is even
# Logic: If a number divided by 2 leaves a remainder of 0, it's even
# is_even = (number / 2 == 0)
is_even = (number % 2 == 0)

print(f"Is the number {number} even? {is_even}")



"""
Q1 . What this code is doing?
Ans: This code is checking if a number is even.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 6th line because the code uses division (`/`) instead of modulo (`%`) to check if a number is even. The consequence is that the result is incorrect.

Q3. How to solve it?
Ans: To solve it we should use the modulo operator (`%`) to check if a number is even: `is_even = (number % 2 == 0)`.




"""