num = 1

for i in range(20,0,-1):
    if num%i != 0:
        num = num*i
        print(i)

print('res',num)        
        
    
