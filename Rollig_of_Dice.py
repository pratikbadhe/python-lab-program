#Rolling of dice 
#name Pratik Badhe 
#M-02 11810754

from random  import randint as rt
out=0
faces=6
dice=1
for roll in range(0,dice):
    out+=rt(1,faces)
print(out)
    
