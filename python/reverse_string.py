def reverse_string(a):
    rev=""
    for i in a:
        rev=i+rev
    return rev
print(reverse_string(input("Enter the string")))