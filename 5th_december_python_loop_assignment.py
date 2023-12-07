#!/usr/bin/env python
# coding: utf-8

# In[1]:


"Question:-1"
for i in range(1,11):
    print(i)


# In[2]:


"Question:-2"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = 0
# Iterate through the list using a for loop
for num in numbers:
    # Add each number to the sum
    sum_of_numbers += num
# Print the result
print("The sum of numbers in the list is:", sum_of_numbers)


# In[3]:


"Question;-3"
input_string = "Deepak singh"
for char in reversed(input_string):
    print(char, end='')



# In[4]:


"Question:-4"
# Python program to calculate the factorial of a given number using a for loop

# Function to calculate factorial
def factorial(n):
    result = 1
    # Use a for loop to calculate the factorial
    for i in range(1, n + 1):
        result *= i
    return result
# Input: The number for which factorial needs to be calculated
number = int(input("Enter a number "))
# Check if the number is non-negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate and print the factorial
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")


# In[5]:


"Question;-5"
def print_multiplication_table(number):
    print(f"Multiplication Table for {number}")
    # Use a for loop to print the table
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
# Input: The number for which multiplication table needs to be printed
number = int(input("Enter a number "))
# Call the function to print the multiplication table
print_multiplication_table(number)


# In[6]:


"Question:-6"
# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0
# Use a for loop to iterate through the list
for num in numbers:
    # Check if the number is even or odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print("Number of even numbers", even_count)
print("Number of odd numbers", odd_count)


# In[7]:


"Question:-7"
# Use a for loop to iterate through numbers from 1 to 5
for i in range(1, 6):
    square = i ** 2
    print(f"The square of {i} is: {square}")


# In[8]:


"Question:-8"
# Function to calculate the length of the string
def string_length(input_string):
    length = 0
    for _ in input_string:
        length += 1
    return length
# Input: The string for which length needs to be calculated
user_input = input("Enter a string")

# Calculate and print the length of the string
length_of_string = string_length(user_input)
print(f"The length of the string is: {length_of_string}")


# In[9]:


"Question:-9"
numbers = [5, 10, 15, 20, 25]
# Initialize variables for sum and count
sum_of_numbers = 0
count = 0
# Use a for loop to iterate through the list
for num in numbers:
    sum_of_numbers += num
    count += 1
# Calculate the average
if count > 0:
    average = sum_of_numbers / count
    print(f"The average of the numbers is: {average}")
else:
    print("Cannot calculate average for an empty list.")


# In[10]:


"Question:-10"
def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers
# Input: The number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))
# Check if n is non-negative
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and print the first n Fibonacci numbers
    fibonacci_sequence = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are {fibonacci_sequence}")


# In[11]:


# Intermeditae level
"Question:-11"
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
my_list = [1, 2, 3, 4, 5, 2]  # Contains duplicates (2)
if has_duplicates(my_list):
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")


# In[12]:


"Question:-12"
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
# Example usage:
start_range = 10
end_range = 50
print(f"Prime numbers in the range {start_range} to {end_range}:")
print_primes_in_range(start_range, end_range)



# In[13]:


"Question:-13"
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
# Example usage:
input_str = "Deepak, Singh!"
result = count_vowels(input_str)
print(f"The number of vowels in the string '{input_str}' is: {result}")


# In[14]:


"Question:-14"
def find_max_element_2d(matrix):
    if not matrix or not matrix[0]:
        return None  # Empty matrix
    max_element = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element
# Example usage:
two_d_list = [
    [1, 5, 3],
    [8, 2, 4],
    [6, 7, 9]
]
max_value = find_max_element_2d(two_d_list)
print(f"The maximum element in the 2D list is: {max_value}")


# In[15]:


"Question:-15"
def remove_element(lst, target):
    updated_list = [item for item in lst if item != target]
    return updated_list
# Example usage:
original_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2
result_list = remove_element(original_list, element_to_remove)
print(f"Original List: {original_list}")
print(f"List after removing {element_to_remove}: {result_list}")


# In[16]:


"Question:-16"
def generate_multiplication_table():
    for i in range(1, 6):
        print(f"Multiplication table for {i}:")
        for j in range(1, 11):
            result = i * j
            print(f"{i} x {j} = {result}")
        print()  # Add a newline between tables
# Call the function to generate the multiplication table
generate_multiplication_table()


# In[20]:


"Question:-17"
def fahrenheit_to_celsius(fahrenheit_temps):
    celsius_temps = []
    for f in fahrenheit_temps:
        celsius = (f - 32) * 5/9
        celsius_temps.append(celsius)
    return celsius_temps
 #Example usage:
fahrenheit_temperatures = [32, 68, 104, 212, 50]
celsius_temperatures = fahrenheit_to_celsius(fahrenheit_temperatures)

for i in range(len(fahrenheit_temperatures)):
   print(f"{fahrenheit_temperatures[i]}°F is {celsius_temperatures[i]:.2f}°C")


# In[21]:


"Question:-18"
def find_common_elements(list1, list2):
    common_elements = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common_elements.append(item1)
                break  # Once a common element is found, break out of the inner loop
    return common_elements
# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements_list = find_common_elements(list1, list2)
if common_elements_list:
    print(f"Common elements: {common_elements_list}")
else:
    print("No common elements found.")


# In[22]:


"Question:-19"
def print_right_triangle_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print('*', end=' ')
        print()
# Example usage:
triangle_rows = 5
print_right_triangle_pattern(triangle_rows)


# In[26]:


def triangle():
    print("*")
    print("* *")
    print("* * *")
    print("* * * *")
triangle()


# In[27]:


"Question:-20"
def find_gcd(num1, num2):
    smaller = min(num1, num2)
    for i in range(smaller, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
# Example usage:
number1 = 48
number2 = 18
gcd_result = find_gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is: {gcd_result}")


# In[28]:


#Advanced Level:
"Question:-21"
def digit_sum(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())
# Example usage:
numbers = [123, 456, 789]
sum_of_digits = [digit_sum(num) for num in numbers]
print(f"Original Numbers {numbers}")
print(f"Sum of Digits {sum_of_digits}")


# In[29]:


"Question:-22"
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_factors(number):
    return [factor for factor in range(2, number + 1) if number % factor == 0 and is_prime(factor)]
# Example usage:
given_number = 84
factors = prime_factors(given_number)
print(f"Prime factors of {given_number}: {factors}")


# In[30]:


"Question:-23"
def extract_unique_elements(input_list):
    return list(set(input_list))
# Example usage:
original_list = [1, 2, 3, 2, 4, 5, 4, 6]
unique_elements = extract_unique_elements(original_list)
print(f"Original List {original_list}")
print(f"Unique Elements {unique_elements}")


# In[31]:


"Question:-24"
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def palindromic_numbers(limit):
    return [num for num in range(limit + 1) if is_palindrome(num)]
# Example usage:
specified_limit = 1000
palindromic_list = palindromic_numbers(specified_limit)
print(f"Palindromic Numbers up to {specified_limit}: {palindromic_list}")


# In[33]:


"Question:-25"
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in (sublist if isinstance(sublist, list) else [sublist])]
nested_list = [[1, 2, [3, 4]], [5, [6, 7]], 8, [9]]
flattened_list = flatten_list(nested_list)
print(f"Nested List {nested_list}")
print(f"Flattened List{flattened_list}")


# In[34]:


"Question:-26"
def sum_even_odd_numbers(input_list):
    even_sum = sum(num for num in input_list if num % 2 == 0)
    odd_sum = sum(num for num in input_list if num % 2 != 0)
    return even_sum, odd_sum

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_sum, odd_sum = sum_even_odd_numbers(numbers_list)
print(f"Original List {numbers_list}")
print(f"Sum of Even Numbers {even_sum}")
print(f"Sum of Odd Numbers {odd_sum}")


# In[35]:


'Question:-27'
odd_squares = [num**2 for num in range(1, 11) if num % 2 != 0]
print(f"Squares of Odd Numbers between 1 and 10: {odd_squares}")


# In[36]:


"Question:-28"
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
combined_dict = {key: value for key, value in zip(keys, values)}
print(f"Combined Dictionary {combined_dict}")


# In[37]:


"Question:-29"
def extract_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for char in input_string if char in vowels]
# Example usage:
input_str = "Hello, World!"
vowel_list = extract_vowels(input_str)
print(f"Original String {input_str}")
print(f"List of Vowels{vowel_list}")


# In[38]:


"Question:-30"
def remove_non_numeric(strings_list):
    return [''.join(char for char in string if char.isnumeric()) for string in strings_list]
# Example usage:
original_strings = ['abc123', '456def', '789ghi', 'jkl']
numeric_only_list = remove_non_numeric(original_strings)
print(f"Original List {original_strings}")
print(f"List with Numeric Characters Only {numeric_only_list}")


# In[39]:


#Challenge Level
"Question:-31"
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
    for number in range(2, int(limit**0.5) + 1):
        if sieve[number]:
            sieve[number*number : limit + 1 : number] = [False] * len(sieve[number*number : limit + 1 : number])
    return [num for num in range(2, limit + 1) if sieve[num]]
# Example usage:
limit = 100
prime_numbers = sieve_of_eratosthenes(limit)
print(f"Prime Numbers up to {limit}: {prime_numbers}")


# In[40]:


"Question:-32"
def pythagorean_triplets(limit):
    return [(a, b, c) for a in range(1, limit + 1)
                      for b in range(a, limit + 1)
                      for c in range(b, limit + 1)
                      if a**2 + b**2 == c**2]
specified_limit = 50
triplets = pythagorean_triplets(specified_limit)
print(f"Pythagorean Triplets up to {specified_limit}: {triplets}")


# In[42]:


"Question:-33"
def generate_combinations(list1, list2):
    return [(item1, item2) for item1 in list1 for item2 in list2]
# Example usage:
list_a = ['a', 'b', 'c']
list_b = [1, 2, 3]
combinations = generate_combinations(list_a, list_b)
print(f"List 1: {list_a}")
print(f"List 2: {list_b}")
print(f"All Possible Combinations: {combinations}")



# In[43]:


"Question:-34"
from statistics import mean, median, mode
def calculate_statistics(numbers):
    return {
        'mean': mean(numbers),
        'median': median(numbers),
        'mode': mode(numbers)
    }
# Example usage:
number_list = [1, 2, 3, 4, 4, 5, 5, 6]
statistics_result = calculate_statistics(number_list)
print(f"Original List: {number_list}")
print(f"Mean: {statistics_result['mean']}")
print(f"Median: {statistics_result['median']}")
print(f"Mode: {statistics_result['mode']}")


# In[44]:


"Question:-35"
def generate_pascals_triangle(rows):
    triangle = [[1] + [sum(pair) for pair in zip(row, row[1:])] + [1] for row in [[1]] * rows]
    return triangle
specified_rows = 10
pascals_triangle = generate_pascals_triangle(specified_rows)
for row in pascals_triangle:
    print(row)


# In[45]:


"Question:-36"
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Example usage:
numbers = [1, 2, 3, 4, 5]
factorial_sums = [sum_of_digits(factorial(num)) for num in numbers]
print(f"Factorials: {[factorial(num) for num in numbers]}")
print(f"Sum of Digits of Factorials: {factorial_sums}")


# In[46]:


"Question:-37"
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)
# Example usage:
input_sentence = "This is a sample sentence to demonstrate the program."
longest = longest_word(input_sentence)
print(f"Original Sentence: {input_sentence}")
print(f"Longest Word: {longest}")


# In[47]:


"Question:-39"
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Example usage:
numbers = range(1, 1001)
digit_sums = [sum_of_digits(num) for num in numbers]
print(f"Sum of Digits for Numbers 1 to 1000 {digit_sums}")


# In[49]:


"Question:-40"
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]
limit = 10000

prime_palindromes = [num for num in range(limit) if is_prime(num) and is_palindrome(num)]

print(f"Prime Palindromic Numbers up to {limit}: {prime_palindromes}")


# In[50]:


"Question:-38"
def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)
string_list = ["hello", "programming", "python", "example", "ai", "OpenAI"]
filtered_list = [word for word in string_list if count_vowels(word) > 3]
print(f"Original List: {string_list}")
print(f"Filtered List (More than 3 vowels): {filtered_list}")


# In[ ]:




