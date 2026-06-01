#for i in range(10,0,-1):
    #print(i)

# for i in range(15,85,1):
#     if i %3 == 0:
#         print("number is divisible by 3:" ,i)
#     else:
#         print("number is not divisible by 3:"  ,i)

mul = 1
for i in range(1,41,1):
    if i % 5 == 0:
        mul=mul*i
        print("number is divisible by 5: " , mul)
    