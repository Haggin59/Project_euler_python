n=0
i=2

while(n!=10001):
       

        flag=1
        for j in range(2,i//2+1):
            
            if i>2 and i%2==0:
                
                flag=0
                break
        
            elif i%j==0:
                
                flag=0
                break
        
        if flag==1:
            #print(i)
            n=n+1
        
        i=i+1

print(i-1)
