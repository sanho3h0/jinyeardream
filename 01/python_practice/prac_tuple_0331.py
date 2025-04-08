fruits = ['cherry', 'apple', 'banana']
# print(list(reversed(fruits[0])))

def reverse(fruit):
    return str(reversed(fruit))

print(sorted(fruits)) #['apple', 'banana', 'cherry']
print(sorted(fruits, key=reverse)) #['cherry', 'apple', 'banana']

print(sorted(fruits)) #['apple', 'banana' , 'cherry']