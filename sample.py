
start =  int(input("Enter starting point"))
end =  int(input("Enter ending point"))

for num in range(start,end): # Input
    # Prime number detection and printing logic
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count = count+1
    if count==2:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")