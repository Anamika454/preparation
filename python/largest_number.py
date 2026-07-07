def largest_number(a):
    large=a[0]
    for i in a:
        if i>large:
            large=i
    return large
print(largest_number([2,86,9,74]))