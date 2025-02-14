marks = {
          "Lovi": 99,
          "Preet": 88,
          "Aman": 77
        }

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Lovi": 100, "Shami": 44})
print(marks)

# print(marks.get("Preet2")) # prints none, Preet2 doesn't exist
# print(marks["Preet2"]) # returns error as not same as above

print(marks.pop("Preet"))
print(marks.popitem())

# d = {} # empty dicitionary
