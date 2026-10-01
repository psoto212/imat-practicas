def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_wrong(n):
    return n * factorial_wrong(n - 1)

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")


