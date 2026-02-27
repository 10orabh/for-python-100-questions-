# Code 5/100
base = 5
power = 3

# Calculating base to the power
# result = base ^ power
result = base ** power

print(f"{base} raised to the power of {power} is: {result}")


"""
Q1 . What this code is doing?
Ans: This code is calculating the power of a base number.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 6th line because `^` is a bitwise XOR operator in Python, not exponentiation. The consequence is that the result is incorrect.

Q3. How to solve it?
Ans: To solve it we should use the `**` operator for exponentiation: `result = base ** power`.




"""