class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


n = int(input("Enter a number: "))
users = list()
for i in range(1, n+1):
    name = input(f"Enter name for {i}th User: ")
    age = int(input(f"Enter email for {i}th User: "))
    user = User(name, age)
    users.append(user)

for user in users:
    if user.age%2==0:
        print(user.name)