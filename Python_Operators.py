'''#Python Operators


#Arithmetic Operators:- Arthmetic Operators are used with numeric values to perform common mathemathical operations.

#1:-  Addition Operator +
add1=10
add2=5
total1=add1+add2
print(total1)


#2:-  Subtraction Operator -
sub1=10
sub2=5
total2=sub1-sub2
print(total2)


#3:-  Multiplication Operator *
mul1=10
mul2=5
total3=mul1*mul2
print(total3)


#4:-  Division Operator /
div1=10
div2=2
total4=div1/div2
print(total4)


#5:-  Remainder/Modulus Operator %
rem1=10
rem2=3
total5=rem1%rem2
print(total5)


#6:-  Exponent(Raised to power) Operator **
exp1=10
exp2=2
total6=exp1**exp2
print(total6)


#7:-  Floor division Operator //
flo1=10
flo2=3
total7=flo1//flo2
print(total7)











#Assignment Operators:- Assignment operators are used to assign values to variables.

#  =
x=10
y=x
print(y)


#1:-   +=  
x=10
x+=20
print(x) 

#or

x1=10
x1=x1+20
print(x1)

#2:-   -=

y=20
y-=10
print(y)

#or

y1=20
y1=y1-10
print(y1)

#3:-   *=

z=10
z*=2
print(z)

#or

z1=10
z1=z1*2
print(z1)



#4:-   /=

a=10
a/=2
print(a)

#or

a1=10
a1=a1/2
print(a1)


#5:-   //=

b=10
b//=2
print(b)

#or

b1=10
b1=b1//2
print(b1)



#6:-   %=

c=10
c%=2
print(c)

#or

c1=10
c1=c1%2
print(c1)


#7:-   **=

d=10
d**=2
print(d)

#or

d1=10
d1=d1**2
print(d1)








#Comparison Operators:- Comparison Operators are used to compare two values.
#1:- Equal ==
x=10
y=20
print(x==y)


#2:- Not Equal !=
x=10
y=20
print(x!=y)


#3:- Greater than    >
x=20
y=10
print(x>y)

#4:- Less than  <
x=10
y=20
print(x<y)


#5:- Greater than or Equal to  >=
x=10
y=10
print(x>=y)


#6:- Less than or Equal to     <=
x=10
y=20
print(x<=y)








#Logical Operators:- Logical Operators are used to combine conditional statements.
#1:- and Operator
x=10
y=20
z=(x<50)and(y<100)
print(z)


#2:- or Operator
x=5
y=10
z=(x>10)or(y>5)
print(z)


#3:- not Operator
x=5
y=10
z=not((x>10)or(y>5))
print(z)

x=10
y=20
z=10
print(id(x))
print(id(y))
print(id(z))
a=x is not y
print((a))







#Bitwise Operators:- Bitwise operators are used to compare (binary) numbers.
#1:- Bitwise and (&)
x=9          #binary 1001
y=9          #binary 1001
z=x & y
print(z)



#2:- Bitwise or (|)
x=9          #binary 1001
y=7          #binary 0111
z=x | y
print(z)


#3:- Bitwise xor ^
x=9          #binary 1001
y=7          #binary 0111
z=x ^ y
print(z)

#4:- Bitwise not  ~


#5:- Bitwise Left Shift    <<
x=9
z=x << 1
print(z)

#6:- Bitwise Right Shift  >>
x=9         #binary 1001
z=x >> 1      #binary 0100
print(z)
'''



