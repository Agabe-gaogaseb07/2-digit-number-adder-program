#Welcome message printed first always.!!
print("Hello and Welcome to my 2 digits number adding program, By Daniel !Gao-!gaseb")

#I created a variable (number) for the number going to be entered.
number = input("Type a two digit number: ")

#Then i add the two using Their values 0 in index form which is 1(0), & (2), which is the second digit. 
number_1 = f"{number}"[0]
number_2 = f" {number}"[2]

#Which then adds the numbers in the number entered.
total = int(number_1) + int(number_2)

#Then print the total.
print(total)


