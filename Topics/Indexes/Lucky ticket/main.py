# Save the input in this variable
ticket = input()

# Add up the digits for each half
for i in ticket:
    index =0
    suma =0
    if index < 1:
        suma = int(i[index]) + suma


    index = index +1
    print(suma)


#half1 = int(ticket[0]) + int(ticket[1])+ int(ticket[2])
#half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
