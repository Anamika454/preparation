def contains_duplicate(a):
    for i in a:
        if a.count(i)>1:
            return(True)
    
    return(False)
print(contains_duplicate([1,2,3,2]))