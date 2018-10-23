#name Pratik Badhe
#roll no. 02
#gr no 11810754
def armstrong(n):
   sum=0
   t=n
   while t>0:
     d=t%10
     sum+=d**3
     t=t//10
   return sum


