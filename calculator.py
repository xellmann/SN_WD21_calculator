print("Welcome to the calculator - lets do some calculations!")

zahl1 = int(input("Please insert your first number: "))
zahl2 = int(input("Please insert your second number: "))
rechenoperation = input("Please insert your arithmetic operation [+ | - | * | / ]: ")

if rechenoperation == "+":
    ergebnis = zahl1 + zahl2
elif rechenoperation == "-":
    ergebnis = zahl1 - zahl2
elif rechenoperation == "*":
    ergebnis = zahl1 * zahl2
elif rechenoperation == "/":
    if zahl2 == 0:
        print("Division durch Null nicht möglich!")
        ergebnis = "undefined"
    else:
        ergebnis = zahl1 / zahl2
else:
    print("Arithmetic operation unknown!")
    ergebnis = "undefined"

print("The arithmetic operation chosen was: " + str(rechenoperation))
print("The result is: " + str(ergebnis))
