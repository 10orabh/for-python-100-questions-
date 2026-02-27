# Code 4/100
math_score = 90
science_score = 80
english_score = 85

# Calculating the average
average_score = math_score + science_score + english_score / 3

print(f"Your average score is: {average_score}")

"""
Q1 . What this code is doing?
Ans: This code calculating the average of the three step.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 5th line because of operator precedence. The division operator has higher precedence than addition, so the expression is evaluated as `math_score + science_score + (english_score / 3)` instead of `(math_score + science_score + english_score) / 3`. The consequence is that the average is calculated incorrectly.

Q3. How to solve it?
Ans: To solve it we should use parentheses to ensure proper order of operations: `average_score = (math_score + science_score + english_score) / 3`.

"""