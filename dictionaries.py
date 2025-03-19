users = [
    {
        "id":1,
        "name": "Someone",
        "age": 19
    },
    {
        "id":2,
        "name": "Another",
        "age": 17
    },
    {
        "id":3,
        "name": "New",
        "age": 20
    }
]

# for user in users:
#     if user['age'] > 18:
#         print(f"{user['name']} -> {user['age']}")

def isPrime(num):
    count = 0
    for i in range(1, num+1):
        if num%i==0:
            count = count + 1
    if count==2:
        return True
    else:
        return False
    
for user in users:
    if isPrime(user['age']):
        print(f"{user['name']} -> {user['age']}")