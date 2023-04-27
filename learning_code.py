# reverse int program
# n = int(input("please give a number : "))
# print("before reverse your numeber is :" ,n)
# reverse = 0
# while n!=0:
#     reverse = reverse*10 + n%10
#     n = (n//10)
# print("after reverse: %d" %reverse)


# Prime Number Program
# num = 11
# if num > 1:
# 	for i in range(2, int(num/2)+1):
# 		if (num % i) == 0:
# 			print(num, " is not prime")
# 			break
# 		else:
# 			print(num, "number is prime")
# else:
# 	print(num, "is not prime")

# Fibonacci series program

n = int(input("Enter the number:"))

a,b = 0,1

if n <= 0:
    print("please enter positive integer")
elif n == 1:
    print("fibo sequence upto",n, ":")
    print(a)
else:
    print("fibo seq:")
    for i in range(n):
        print(a)
        c = a+b
        a ,b = b, c
