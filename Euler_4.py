
largest_value = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        product = i*j
        
        str1 = str(product)
        str2 = str1[::-1]
        if str1 == str2:
            if product>largest_value:
                largest_value = product
                
                
print(largest_value)        
