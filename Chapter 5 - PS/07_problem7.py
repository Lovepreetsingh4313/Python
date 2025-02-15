# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}

# You cannot add a list directly to a set because lists are mutable and unhashable
# If you need a mutable collection inside a set, use tuples (immutable collections) instead of lists
# Sets themselves are mutable: You can modify the set (add/remove items)
# Elements inside the set must be immutable and hashable: For example, you can have integers, strings, and tuples as elements, but not lists or dictionaries