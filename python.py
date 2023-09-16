# 2.list1=["apple","banana","cherry"]
# print element in index 2
# update banana to mango
# delete cherry form list
# cpmbine list1 with list2=("kiwi","orange") 
list1 = ["apple","banana","cherry"]
print(list1[2])

list1[1] = "mango"
print(list1)

list1.remove("cherry")
print(list1)


list2=("kiwi","orange") 
list1.extend(list2)
print(list1)

# 3. Write a Python program to remove duplicates from a list

a = [10,20,30,30,20,60,50,50,40,40,60]
duplicate = set()
uinque = []
for x in a:
    if x not in duplicate:
        uinque.append(x)
        duplicate.add(x)
print(duplicate)


# Write a Python program which accepts the radius of a circle from the user and compute the are
pie = 3.14
Radius = float(input("Please enter area of circle"))

area_of_the_circle = pie*Radius*Radius
print("The Area circle:",area_of_the_circle)