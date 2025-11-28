'''#List

list1=["Nitesh","Age",21]
print(list1)


#Access Items
list2=["Apple","Banana","Cherry"]
print(list2[1])

#Change Item Value
list1=["apple","banana","cherry"]
print(list1)
list1[1]="grapes"
print(list1)

#Check if item exists
list1=["apple","banana","cherry"]
if "apple" in list1:
  print("Yes")


#Remove item
list1=["apple","banana","cherry"]
list1.remove("banana")
print(list1)


#Pop() Method
list1=["apple","banana","cherry"]
list1.pop()
print(list1)

#del
list1=["apple","banana","cherry"]
del list1[0]
print(list1)


#clear
list1=["apple","banana","cherry"]
list1.clear()
print(list1)


#copy()  change item
list1=["apple","banana","cherry"]
list2=list1
list1.remove("banana")
print(list2)


#copy() item not change
list1=["apple","banana","cherry"]
list2=list1.copy()
list1.remove("apple")
print(list1)
print(list2)

#copy()
list1=["apple","banana","cherry"]
list2=list(list1)
print(list2)

#Nested list
list1=["Nitesh",[10,20,30]]
print(list1)


#List Repetition *
list1=[10,20,30]*2
print(list1)


#Concatenate the list  +
list1=[10,20,30]
list2=[40,50,60]
print(list1+list2)


#len()
list1=[10,20,30]
print(len(list1))


#sum()
list1=[10,20,30]
print(sum(list1))

#append
list1=[10,20,30]
list1.append("nitesh")
print(list1)

#count()
list1=[10,20,30,10,40,10,50]
print(list1.count(10))


#max
list1=[10,20,30,40,50]
print(max(list1))

#min
list1=[10,20,30,40,50]
print(min(list1))

#sort()
list1=[10,5,20,15,30,35,70,50,40]
list2=list1.sort()
print(list1)
'''












