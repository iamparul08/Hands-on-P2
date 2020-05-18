
mylist3_ADID = ["Python", "Java", "Swift", "C++", "JavaScript"]
print("List containing 5 elements")
for i in range(len(mylist3_ADID)):
    print(mylist3_ADID[i])

#add one element "Banglore" at the beginning of the list

print("Banglore is added at he beginning of the list")
mylist3_ADID.insert(0, "Banglore")

for i in range(len(mylist3_ADID)):
    print(mylist3_ADID[i])

#remove one element from the end
print("Removing one element from the end")
mylist3_ADID.remove("JavaScript")
for i in range(len(mylist3_ADID)):
    print(mylist3_ADID[i])