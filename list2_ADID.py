
mylist2_ADID = [10, 30, 50, 20, 40, "Wipro", "TCS", "IBM", "HCL", "Accenture"]
print("list containing 10 elements")
for i in range(len(mylist2_ADID)):
    print(mylist2_ADID[i])

#add one element 100 at the end of the list
mylist2_ADID.append(100)
print("100 is added at the end of the list")
for i in range(len(mylist2_ADID)):
    print(mylist2_ADID[i])

#add one element "Wipro" at the end of the list

mylist2_ADID.append("Wipro")
print("Wipro is added at the end of the list")
for i in range(len(mylist2_ADID)):
    print(mylist2_ADID[i])
