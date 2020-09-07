values = [66, 43, 1, 6, 2, 99, 4]

for bob in values:
    if bob <= 10:
        print (bob)


position = 0
while(len(values) > position):
    bob = values[position]
    if bob <= 10:
        print (bob)
    position = position + 1