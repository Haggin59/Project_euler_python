#Longest Collatz sequence
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Which starting number, under one million, produces the longest chain?

n = 0
count = 1
max_count = 0
no = 0
#print(n)

for i in range(1,1000000):
    count = 1
    n = i
    #print(n,'---')
    while n!= 1:
        
        if n%2 == 0:
            n = n/2
            #print(n)
        else:
            n = (3*n) + 1
            #print(n)
        count += 1
    #print('count:',count)
    if count > max_count:
        max_count = count
        no = i


print('====')
print(max_count)
print(no)

        
