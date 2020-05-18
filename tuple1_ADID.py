
#printing the elements in tuple
mytuple1_ADID = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Values in tuple")
for i in range(len(mytuple1_ADID)):
    print(mytuple1_ADID[i])

#adding 100
print("adding 100 to this tuple after converting into list")

#mytuple1_ADID[1] = 100

#since tuple is immutable datatype
l1 = list(mytuple1_ADID)
for i in range(len(l1)):
    print(l1[i])

l1.append(100)
for i in range(len(l1)):
    print(l1[i])
