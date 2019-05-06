a,b = 1,2
c = a + b
sum = 0
for c in range (1,4000000):
    if(c % 2 == 0):
        sum = sum + c
        a = b 
        b = c
        c = a + b
print(sum)
        
