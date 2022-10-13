#Find the sum of all the primes below two million
n=3
sum=2
flag = 1
while(n<2000000):
    flag=1
    
    for i in range(2,n//2+1):
       

        if n%i == 0:
            flag=0
            break

    if(flag==1):
        print(n)
        sum+=n    

    n=n+2
print(sum)    
        



