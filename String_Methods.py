
#strip()
#Example the strip() method removes any whitespace from the beginning or the end.
a="    Nitesh Gupta    "
print(a.strip())
'''

#lstrip()
#The lstrip() method removes any leading characters by left space as the leading character.
b="      Avinash Gupta"
print(b.lstrip())


#rstrip()
#The rstrip() method removes any leading characters by right space as the leading character.
c="Abhishek Gupta               "
print(c.rstrip())


#lower()
#Example the lower() method returns the string in lowercase.
e="LOWER CASE"
print(e.lower())


#len()
#Example the len() method returns the length of a string.
d="nitesh gupta"
print(len(d))


#upper()
#Example the upper() method returns the string in uppercase.
f="upper case"
print(f.upper())

#Capitalize()
#Capitalizing the first character of the string.
g="capitalize harikesh gupta"
print(g.capitalize())

#title
#Example the title() converts the first character of each word to upper case.
h="my name is nitesh gupta"
print(h.title())


#count()
#Example the count() returns the number of times a specifird value occurs in a string.
i="mithilesh gupta"
print(i.count("i"))


#find()
#Example the find() searches the string for a specified value and returns the position of where it was found.
j="Nitesh Gupta"
print(j.find("G"))


#replace()
#Example the replace() method replaces a string with another string.
k="Nitesh Gupta"
print(k.replace("Gupta","Bhai"))


#split()
#Example the split() method splits the string into substrings if it finds instances of the separator.
l="niatesh gupta"
print(l.split("a"))


#startswith()
#If string is started with passed value startswith() method returns true if not then returns false.
m="nitesh gupta"
print(m.startswith("n"))


#endswith()
#Returns true if string endswith a specified value. Otherwise it returns false.
n="Nitesh Gupta"
print(n.endswith("G",2,8))


#isalnum()
#If all the characters are alphanumeric (alpabet a-z and number 0-9) the isalnum() method returns true.
o="Nitesh18"
print(o.isalnum())

#or

p="Nitesh 18"
print(p.isalnum())

#isdigit()
#If all the characters are numeric the isdigit() method returns true, otherwise false.
q="1234"
print(q.isdigit())

#or

r="12nitesh"
print(r.isdigit())

s="12 22"
print(s.isdigit())


#isupper()
#If all the characters are in uppercase then the isupper() method returns true or else false.
t="NITESH GUPTA"
print(t.isupper())


#islower()
#If all the characters are in lowercase them islower() method returns true otherwise return false.
u="nitesh gupta"
print(u.islower())
'''



