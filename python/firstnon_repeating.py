def non_repeating(a):
    for i in a:
        if a.count(i)==1:
            return i
print(non_repeating("leetcode"))