def factorial(num):
    fact = 1
    while num > 0 :
        fact = fact * num
        num -= 1
    return fact
num = int(input("Enter the number to calculate its factorial "))
print(f"Facorial of {num} is {factorial(num)}")