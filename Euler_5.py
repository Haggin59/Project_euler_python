
least_value = 0
i = 2520

while True:
    flag = 1
    for j in range (20,0,-1):
        if i%j!=0:
            flag = 0
            break
    if flag == 1:
        least_value = i
        break
    else:
       # print (i)
        i=i+2520
        
         
print("Num: ",least_value)
