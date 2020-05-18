
#creating tuple consisting of 5 elements

mytuple2_ADID = ("Desktops", "Mobiles", "Laptops", "Bluetooths", "Headphones")
for i in range(len(mytuple2_ADID)):
    print(mytuple2_ADID[i])

#printing the first element of tuple
print("\nFirst value of tuple is ")
print(mytuple2_ADID[0])

mytuple1_ADID[1] = 100 #here is error cz tuple is immutable datatype i.e. contents can not be altered
#so we can not add 100 like this