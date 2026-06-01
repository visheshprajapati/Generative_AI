#age=18
#if age >= 18:
    #print ("you are an adult.")
#else:
    #print("you are a minor.")


#age=(int)(input("enter your age :"))
#if age >= 18:
    #print ("you are an adult.")
#else:
    #print("you are a minor.")


#marks=(int)(input("enter your marks :"))
#if marks >=90:
    #print("grade : A")
#elif marks >=80:
    #print("grade : B")
#else:
    #print("grade : C")

#a=int(input("enter your number:"))
#b=int(input("enter anothor number:"))
#c=int(input("enter third number:"))
#if a > b and a > c:
    #print("the largest number is :", a)
#elif b > a and b > c:
    #print("the largest number is :", b)
#else:
    #print("the largest number is :", c)

# a=int(input("enter your number"))
# b=int(input("enter your number"))
# c=int(input("enter your number"))
# if a+b>c
#     print("its a tringle")
# else:
#     print("its a not tringle")

import sys
a=(int)(input("enter a first value :"))
b=(int)(input("enter a secound value :"))

if b<a:
    print("invalid value : ")
    sys.exit(1)

c=input("enter opration: ")

if c == "add":
    print("addition : " , a+b)
elif c == "sub":
    print("substraction : " , a-b)
elif c == "mul":
    print("multipliication : " , a*b)
elif c == "div":
    print("division : " , a/b)
