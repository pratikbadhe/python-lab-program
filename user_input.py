

def facto(x): 
   if x==0:
      print("1")
   elif x==1:
      print("1")
   else:
      multi=1
      for i  in range (2,x+1,1):
        multi=multi*i
      print(multi)
x=int(input("enter a number"))
m=facto(x)

