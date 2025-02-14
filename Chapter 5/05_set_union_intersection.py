s1 = {1, 5, 7, 21, 9}
s2 = {11, 15, 17, 19, 9, 21}

print(s1.union(s2))

print(s1.intersection(s2))

print({1, 21}.issubset(s1))
print({1, 5, 7, 21, 9}.issuperset(s1))