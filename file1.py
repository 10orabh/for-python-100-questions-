# Code 1/100
user_age_input = "25"
years_to_add = 5

# future_age = user_age_input + years_to_add 
future_age = int(user_age_input) + years_to_add

# print("In 5 years, you will be: " + future_age)
print(f"In 5 years, you will be: {future_age}")

"""
Q1 . What this code is doing?
Ans: This code is taking two variable value and add them and print the result.

Q2. is there is bug and what causes it and what are the consequences.
Ans: Yes bug is present in 5th line causes by first line type and also present in 7 line same type of bug is present And the consequences is the type error causes by both bugs.

Q3. How to solve it?
Ans: To solve it we shoud type cast the variable user_age_input in line one or in line 5 where we add it.And also we should add f string or tyep cast the future_age variable with string 

"""
