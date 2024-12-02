# tup = (1, 5, 4, 9)
# print(type(tup), tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])


# countries = ("India", "England", "Russia", "Spain", "Italy")
# temp = list(countries)
# temp.append("Bhutan")  #Add item
# temp.pop(2) #Remove item
# temp[3] = "Germany" #Change item
# countries = tuple(temp)
# print(countries)


# countries = ("India", "England", "Japan", "Bhutan")
# countries1 = ("Nepal", "China", "Spain")
# Total = countries + countries1
# print(Total)


tuple1 = (1, 2, 7, 3, 6, 4, 3, 2, 3, 2, 3)
# res = tuple1.count(3) # [same elements count]
res = tuple1.index(3) #position of digit
print('Count of 3 in tuple1 is :', res)