""" n = int(input("Enter a number: "))

numbers = list()

for i in range(1, n+1):
    temp = int(input(f"Enter {i}th Number: "))
    numbers.append(temp)

print(numbers) """

numbers = [n for n in range(1, 6) if n%2==0]

print(numbers)
