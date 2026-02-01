micset={1,2,2,3,4,4,4}
print("Set :", micset)
micset.add(5)
print("Updated Set:", micset)
set1=micset
set2={2,4,4,6}
print("\nSet 1", set1)
print("Set 2", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric_difference(set2))