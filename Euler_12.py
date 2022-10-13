#Triangle no with 500 factors
import math
n = 1
while True:
    factor_count = 0
    t_no = int((n*(n+1))/2)

    #print(t_no)

    for i in range(1,int(math.sqrt(t_no)+1)):

        if t_no % (i) == 0:
            factor_count += 1
            if i != math.sqrt(t_no):
                factor_count += 1
    
    if factor_count >= 500:
        print(t_no)
        break    
    
    n += 1


 