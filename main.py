"""
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
print(b.convert_to_btc(60000,'EUR'),"Btc")
"""



"""
a = int(input("enter the number of line:"))
for i in range(a) :
    for j in range(1,i+2):
        print(j,end="")
    print("")
for i in range(a):
    for j in range(1,a):
        print(j, end="")
    print("")
    a-=1
"""

"""
a = int(input("enter the number of line:"))
for i in range(a) :
    j=0
    for j in range(1,i+2):
        print(j,end=" ")
    for j in range(a-i-1):
            print("   ",end=" ")
    for j in range(i + 2,1,-1):
                print(j-1, end=" ")
    print("")
"""

"""
C = int(input("entrez le nombre de colonnes :"))
x=C
k=2
for i in range(C):
    y=k
    for j in range(1,x):
        print(" ",end="")
    x-=1
    for j in range(1,i+1):
        print(i-j+1,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

"""

"""
a = int(input("enter the number of line:"))
k=1
for i in range(1,a+1) :
   if k==1:
    for j in range(1,i+1):
        print(k,end="")
        if k == 1:
            k -= 1
        else:
            k += 1
    print("")
   else:
       k=1
       for j in range(1, i + 1):
           print(k, end="")
           if k == 1:
               k -= 1
           else:
               k += 1
       print("")

       1
       10
       101
       1010
"""

"""
a = int(input("enter the number of line:"))
for i in range(1,a+1) :
    for j in range(1,i+1):
        print(j,end="")
    print("")
"""

"""
a = int(input("enter the number of line:"))
for i in range(1,a+1) :
    for j in range(i):
        print(i,end="")
    print("")
"""#triangle avec des numbers

"""
L = int(input("entrez le nombre de ligne :"))
C = int(input("entrez le nombre de Colonne :"))

k=1
for i in range(1,L+1):
    for j in range(C):
        print(i,end="")
    print("")
    k+=1

    111111111111111
    222222222222222
    333333333333333
    444444444444444
"""
