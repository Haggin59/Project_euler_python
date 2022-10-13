#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
fhand = open('euler.txt')

z = []

for line in fhand:
    z.append(int(line))

print(sum(z))
    