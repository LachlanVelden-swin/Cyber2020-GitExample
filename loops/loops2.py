# Write a program that totals every number between and including 10 and 50, and outputs the subtotal on a separate line.

# Write a program that totals all of the numbers between and including 5 and 50 that are divisible by 5.

total = 0

count = 5
while (count <= 5000000000):
    if(count % 5 == 0):
        total = total + count
    count = count + 1

print("Total is " + str(total))
