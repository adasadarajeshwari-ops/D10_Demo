x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
z=int(input("Enter the number:"))
if x+y+z==180:
   print("yes we can form a triangle")
   if x==y==z:
      print("It is a equalent triangle")
   elif x==y or y==z or x==z:
      print("It is a isosceles triangle")
   else:
      print("scalene triangle")
else:
      print("can not form a triangel")

