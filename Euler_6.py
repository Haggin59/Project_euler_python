sum_of_squares = 0
square_of_sum = 0
temp = 0
for i in range(1,101):
    sum_of_squares = sum_of_squares + (i*i)
    temp = temp + i
    
square_of_sum = temp*temp     

print(sum_of_squares)
print(square_of_sum)
print(square_of_sum-sum_of_squares)

    
