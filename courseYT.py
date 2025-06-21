print("Hello", "world!", sep=",")
print("first row", end=" ")
print("second row")



def get_apartment_number():
    entrance = [1, 2, 3, 4, 5]
    apartment = input("Enter apartment number: ")
    if apartment.isdigit():
        apartment = int(apartment)
        if 1 <= apartment <= 100:
            entrance_index = (apartment - 1) // 20
            entrance_number = entrance[entrance_index]
            position_in_entrance = (apartment - 1) % 20
            floor_number = position_in_entrance // 4 + 1
            print(f"Entrance: {entrance_number}, Floor: {floor_number}")
        else:
            print("Apartment number must be between 1 and 100.")

print("Welcome to the apartment number finder!")


