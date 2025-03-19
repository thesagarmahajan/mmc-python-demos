# def greet(name, age=18):
#     return f"Welcome, {name} with age = {age}"

# print(greet(age=20, name="Sagar"))

# def numbers(*n):
#     return list(n)

# print(type(numbers(12,34,65,778,321,698,3243,54)))

# def sample(*args, **kwargs):
#     """
#         This function does nothing!
#         How to invoke the function?
#         -> sample(val1, val2, val3, key1=val1, key2=val2)
#     """
#     pass

# res = sample(name="Someone", age=25, email="someone@example.com")
# print(type(res))
# sample(name="Someone", age=25, email="someone@example.com")
# print(sample.__doc__)

def customRange(start, end):
    while start<end:
        start+=1
        yield start

# for i in customRange(1,10):
#     print(i)

print(customRange(1,10))