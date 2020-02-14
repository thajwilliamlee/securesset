#print(int("four"))
print("Welcome to our calculator")
print()
problem = input("What is your math problem? ")
results = ""
numbers= []
operators= []
for i in problem:
    if i.isdigit():
        numbers.append(i)
    else:
        operators.append(i)

for i in operators:
    if i == "*" or i == "/":
        temp = operators.index(i)
        if i == "*":
            results = int(numbers[temp]) * int(numbers[temp + 1])
        elif i == "/":
            results = int(numbers[temp]) / int(numbers[temp + 1])
        numbers.remove(numbers[temp])
        numbers.remove(numbers[temp])
        numbers.insert(temp,results)

    elif i == "+" or i == "-":
        if i == "+":
            results = int(numbers[0]) + int(numbers[1])
        elif i == "-":
            results = int(numbers[0]) - int(numbers[1])
        numbers.remove(numbers[0])
        numbers.remove(numbers[0])
        numbers.insert(0,results)



print(numbers)
print(operators)



print(problem)
print(results)
