# Q4.
# Create a set of 10 fruits.
# Create another set of summer fruits.
# Create another set of winter fruits.
# Perform the following operations:
# i) Print all fruits in the 3 sets.
# ii) Print fruits common in fruits and winter fruits.
# iii) Print fruits only in summer fruits but not in fruits.
# iv) Print fruits present in summer and winter but not in fruits.
# v) Check whether Orange exists in fruits.
# vi) Find in which set Pineapple exists.

fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes",
          "Pineapple", "Guava", "Papaya", "Kiwi", "Pear"}

summer = {"Mango", "Watermelon", "Litchi", "Muskmelon", "Pineapple"}

winter = {"Orange", "Apple", "Strawberry", "Guava", "Kiwi"}

print("Fruits:", fruits)
print("Summer Fruits:", summer)
print("Winter Fruits:", winter)

print("\nCommon in Fruits & Winter:", fruits.intersection(winter))

print("Only in Summer:", summer - fruits)

print("Summer and Winter but not Fruits:",
      (summer.intersection(winter)) - fruits)

if "Orange" in fruits:
    print("Orange is present in Fruits set.")
else:
    print("Orange is not present.")

print("\nPineapple found in:")
if "Pineapple" in fruits:
    print("- Fruits Set")
if "Pineapple" in summer:
    print("- Summer Set")
if "Pineapple" in winter:
    print("- Winter Set")