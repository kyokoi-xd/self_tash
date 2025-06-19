items = [3, 2, 1, 0]
for item in items:
    print(item)


guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print("too low")
    else:
        print("found it!")
    number += 1

guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
