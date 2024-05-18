# age = int(input("enter your age:-"))
# if age>=18:
#     print("you can give a vote")
# else:
#     print("you cannot give a vote")


# sub1 = int(input("hindi:-"))
# sub2 = int(input("maths:-"))
# sub3 = int(input("english:-"))
# total = sub1+sub2+sub3
# a = total//3
# print("total:-",total)
# print("per:-",a)
# if  total>=80:
#     print("A")
# elif total>70:
#     print("B")
# elif total>40:
#     print("C")
# else:
#     print("fail try next time""per:-",a)


# a  = int(input("enter any number:-"))
# if a>0:
#     print("it is a positive number")
# else:
    # print("is is negative number")


# a = int(input("enter any numbers and check odd an even:-"))
# if a % 2 ==1:
#     print("odd",a)
# else:
#     print("even",a)



# a = int(input("enter any numbers and check odd an even:-"))
# if a % 2 ==0:
#     print("even",a)
# else:
#     print("odd",a)




a = int(input("enter any number:-"))
b = int(input("enter any number:-"))
c = int(input("enter any number:-"))
d = int(input("enter any number:-"))
e = int(input("enter any number:-"))
if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
elif c>d and c>e:
    max=c
elif d>c and d>e:
    max=d
else:
    max=e
print(max)