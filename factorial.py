def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):  # Loop from 2 to n
        result *= i
    return result

num = int(input("enter ur no : "))
print("The factorial of", num, "is", factorial_iterative(num))
 