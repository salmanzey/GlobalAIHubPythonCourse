mylist = [5, 8, 98, 45, 7, 85, 99, 75]
mylist1 = mylist[0 : 4]
mylist2 = mylist[4 : 8]
mylist2.extend(mylist1)
print(mylist2)