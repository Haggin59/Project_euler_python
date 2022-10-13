
n=600851475143
for i in range(2,n):
    if n%i ==0:
        flag=1
        for j in range(2,(i//2)+1):
            if i>2 and i%2 == 0:
                flag=0
                break
            
            if i%j == 0:
                flag = 0
                break
        
        if flag == 1:
            print(i)
            
