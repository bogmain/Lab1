
# base=12
#
# i = int(s,base=8)  #база 12
# print(i)
s= int(input("Число 1: "))
b= 12 #Cистема числення
y= s//12  #ділимо націло
n= s%12 #знаходимо остачу

c= y//12 #ділимо націло
f= y%12 #знаходимо остачу

d= c//12  #ділимо націло
if d ==0:
    d = ""
    print(d)
l= c%12  #знаходимо остачу
if l ==0:
    l=""
    print(l)


print(d,l,f,n)   # результат


