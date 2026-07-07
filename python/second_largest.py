#Second largest element
def second_largest(a):
    large=a[0]
    second=a[0]
    for i in a:
        if i>large:
            second=large
            large=i
        elif i>second and i!=large:
             second=i
    return second
print(second_largest([10,5,20,15,8]))