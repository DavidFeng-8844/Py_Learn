my_nums = ((5, 10, 15, 20),  (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))

odd_nums = []
for nums in range(1,51):
    if nums % 2 != 0:
        odd_nums.append(nums)
	
user_input = input("Please input a string with both numeric and alphabetic characters:")
numeric_values = []
alphabets = []

# Iterate over each character in the input string
for char in user_input:
    if char.isdigit():
        # If the character is a numeric value, add it to the numeric_values list
        numeric_values.append(char)
    elif char.isalpha():
        # If the character is an alphabet, add it to the alphabets list
        alphabets.append(char)

# Create a list with two sublists
result_list = [numeric_values, alphabets]

# Print the final list
print("Result List:", result_list)