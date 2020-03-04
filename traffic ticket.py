speed = float(input("At what speed is the car?"))
if speed >80:
    print("Fined! You have exceeded the allowed limit of 80 km / h")
    fine = (speed-80) * 7
    print("You must pay a fine of R $ {: 2f}.!".format(fine))
print(" Have a nice day, drive safely! ")