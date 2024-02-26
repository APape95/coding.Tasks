def display_citys():
    """Displays the city options to the user."""
    print("Where would you like to go on holiday?")
    print("1. Spain")
    print("2. Germany")
    print("3. Portugal")
    print("4. Greece")
    print("5. France")
    print("6. Exit")

def get_user_choice():
    """Asks the user to select a destination and returns their choice."""
    while True:
        display_citys()
        des_choice = input("Enter your choice: ")
        if des_choice in ['1', '2', '3', '4', '5', '6']:
            return des_choice
        else:
            print("Invalid choice. Please select a number bettween 1 and 6.")

def plane_cost():
    """Calculates the cost of the plane ticket based on user's choice."""
    user_choice = get_user_choice()
    if user_choice == '1':
        return 100
    elif user_choice == '2':
        return 200
    elif user_choice == '3':
        return 300
    elif user_choice == '4':
        return 400
    elif user_choice == '5':
        return 500
    else:
        return 0


def hotel_cost():
    """Calculates the total cost for the hotel stay."""
    num_nights = int(input("How many nights do you want to stay?"))
    return num_nights * 300

def car_rental():
    """Calculates the total cost for the car rental."""
    rental_days = int(input("How many days car rental do you want?"))
    return rental_days * 150

def holiday_cost():
    """Calculates the total holiday cost."""
    flight_cost = plane_cost()
    hotel_total = hotel_cost()
    rental_total = car_rental()
    total_cost = flight_cost + hotel_total + rental_total
    print(f"Your entire holiday will cost £{total_cost:.2f}")

holiday_cost()