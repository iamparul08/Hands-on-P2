
mydict2_ADID = {
    "Banglore" : 1,
    "Chennai" : 2,
    "Kochi" : 3
}
print(mydict2_ADID)

dict1 = {
    "Hyderabad" : 4
}
print("\nAdding new element Hyderabad")
mydict2_ADID.update(dict1)
print(dict1)

print("\nDelete key Kochi")
mydict2_ADID.pop("Kochi")
print(mydict2_ADID)

print("\nDeleting all elements of the dictionary")
mydict2_ADID.clear()
print(mydict2_ADID)