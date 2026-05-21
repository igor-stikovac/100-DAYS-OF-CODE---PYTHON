import header
import functions

ind = 'n'
result = 0
while ind != 'e':
    if ind == 'c':    
        num_1 = result
        operation = input("Which operation do you want to perform? (+, -, *, /): ")
        num_2 = float(input("What is the second number? "))
        result = functions.operations[operation](num_1, num_2)
    elif ind == 'n':
        num_1 = float(input("What is the first number? "))
        operation = input("Which operation do you want to perform? (+, -, *, /): ")
        num_2 = float(input("What is the second number? "))
        result = functions.operations[operation](num_1, num_2) 
    
    print(f"{num_1} {operation} {num_2} = {result}")

    ind = input("Press 'c' to conitune calculating with {result} or 'n' to start a new calculation, or 'e' to exit\n")
