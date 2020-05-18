mylist4_ADID = [1, 2, 3, 4, 5]
for i in range(len(mylist4_ADID)):
    print(mylist4_ADID[i])

#using reverse method on the list

print("Reversing the list")
mylist4_ADID.reverse()
for i in range(len(mylist4_ADID)):
    print(mylist4_ADID[i])

#creating another list
m1_ADID = [5, 10, 15]

#adding this list at the end of the mylist4_ADID list

print("Second list after the first")
mylist4_ADID.append(m1_ADID)
for i in range(len(mylist4_ADID)):
    print(mylist4_ADID[i])
