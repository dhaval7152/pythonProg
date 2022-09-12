def factorial(no):
    if no==1 or no==0:
        return 1
    else:
        return no*factorial(no-1)

print(factorial(5))
