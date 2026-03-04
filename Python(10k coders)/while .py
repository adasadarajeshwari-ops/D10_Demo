# num=14
# x=1
# while x<num:
#     if num%x==10:
#         print(x)
#     x+=1

# num=6
# x=1
# sum=0
# while x<=num//2:
#     if num%x==0:
#         print(x)
#         sum+=x
#     x+=1
# if sum==num:
#     print("it is perfect number")
# else:
# #     print("it is not perfect number")

# num=16
# x=1
# while x*x<=num:
#     if x*x<=num:
#         print("Perfect square")
#     x+=1
# else:
#         print("Not a perfect square")
# x = 7 
# y = 0 
# print(x and y or 10) 
# num = 405 
# total = 0 
# while num > 0: 
#  total += num % 10 
#  num //= 10 


# # s = "education" 
# # print(s.count("e")) 
# # # print(total) 
# x=112233
# count=0
# while x>0:
#     ld=x%10
#     count+=1
#     x=x//10
# print(count)


# ticket=int(input("Enter the age:"))
# if ticket<5:
#     print("Free")
# elif ticket<=60:
#     print("Full ticket")
# else:
#     print("Discount")
emp={"name":"Raji","Status":"Present","name":"Rani","Status":"Present","name":"Pranay","Status":"Present"}
for x in emp:
    if x["status"]=="Present":
     print(x)