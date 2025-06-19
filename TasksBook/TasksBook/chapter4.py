secret = 7
if guess := 1 > secret:
    print("too high")
elif guess < secret:
    print("too low")
else:
    print("just right")

small = True
green = True

if small:
    if green:
        print("It's peas")
    else:
        print("It's cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
