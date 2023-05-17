# n = int(input("Enter number:"))
#
# result =0
# sign = 1
#
# for i in range(n):
#     result += (n-i)**2
#     temp = result * sign
#     sign = -sign
#
# print (result)

# 1. Write a program that asks the user to enter their name and age, and then outputs a message that says "Hello [name], you are [age] years old!"
# name = input("enter your name:")
# age = int(input("enter your age:"))
#
# print("Hello", name , "your age is", age)

# 2. Write a program that takes a number as input and outputs its square.
# n = int(input("enter Number:"))
# square = n**2
# print(square)

# 3. Write a program that takes two numbers as input and outputs their sum.

# n1 = int(input("enter numaber 1:"))
# n2 = int(input("enter number 2:"))
#
# sum = n1+n2
#
# print(sum)

# 4. Write a program that takes a list of numbers as input and outputs the largest number in the list.

# numbers = [0, 5, 8, 10, 60]
# largest_number = numbers[0]
#
# for num in numbers:
#     if num > largest_number:
#         largest_number = num
#
# print("this is a big number:", largest_number)

# 5. Write a program that takes a string as input and outputs the number of vowels in the string.
# string = input("enter string:")
# vowels = "aeiouAEIOU"
#
# count = 0
#
# for char in string:
#     if char in vowels:
#         count =+ 1
# print("total vowels is:", count)



# 6.Write a program that takes a sentence as input and outputs the number of words in the sentence.

# sentence = input("enter sentence:")
#
# word = sentence.split(" ")
#
# num_word = len(word)
#
# print("total number of word is:", num_word)

# 7. Write a Python function that takes in a list of integers and returns the sum of all the even numbers in the list.


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # Initialize a variable to store the sum
# total = 0
#     # Loop through each number in the list
# for num in lst:
#         # Check if the number is even
#     if num % 2 == 0:
#             # If it's even, add it to the total
#         total += num
#     # Return the final sum
# print(total)


# lst1 = [5, 2, 10, 20]
#
# product = 0
#
# for num in lst1:
#     if num % 2 == 0:
#         product -= num
# print(product)


# 8. Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
#
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# 9. Factorial of a Number:

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, zero, or positive
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("Factorial of", num, "is", factorial)

