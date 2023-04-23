import json

print("WELCOME TO HANISH AMMO-NATION")
print("=========================")

shopping_cart = {
    "SMG-1": 0,
    "Magnum 5.0 Sniper": 0,
    "AK-203": 0,
    "Machine Gun": 0,
    "Shot Gun": 0

}

while (True):
    print("MENU : \n===================")
    print("1. Rifles")
    print("2. Machine Gun")
    print("3. Shot Gun")
    print("4. Exit")

    option_value = int(input("Choose One Option : "))

    if option_value == 1:
        while (True):
            print("Available Rifles : ")
            print("1. SMG-1")
            print("2. Magnum 5.0 Sniper")
            print("3. AK-203")
            print("4. Done")

            sub_option = int(input("Choose Your Rifle : "))

            if sub_option == 1:
                shopping_cart["SMG-1"] += 1
            elif sub_option == 2:
                shopping_cart["Magnum 5.0 Sniper"] += 1
            elif sub_option == 3:
                shopping_cart["AK-203"] += 1
            elif sub_option == 4:
                print("Your Shopping Cart : ")
                print(json.dumps(shopping_cart, indent=4))
                break

    elif option_value == 2:
        shopping_cart["Machine Gun"] += 1
        print("Your Shopping Cart : ")
        print(json.dumps(shopping_cart, indent=4))

    elif option_value == 3:
        shopping_cart["Shot Gun"] += 1
        print("Your Shopping Cart : ")
        print(json.dumps(shopping_cart, indent=4))

    elif option_value == 4:
        print("Thanks for shopping..")
        exit(0)  # exit with success
    else:
        print("Invalid Option")
