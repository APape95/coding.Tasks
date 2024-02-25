# Asking to user how many people.
num_of_people = int(input("How many of you are going on holiday?"))

# Create a def of citys that we can recall later.
def display_citys():
    """Displays the city options to the user."""
    print("Where would you like to go on holiday?")
    print("1. Spain")
    print("2. Germany")
    print("3. Portugal")
    print("4. Greece")
    print("5. France")
    print("6. Exit")

# Asking the user to select an option, storing as variable.
# This will loop until they pick 1 to 6.
def get_user_choice():
    while True:
        display_citys()
        des_choice = input("Enter your choice: ")
        
        if des_choice in ['1', '2', '3', '4', '5', '6']:
            return des_choice
        else:
            print("Invalid choice. Please select a number bettween 1 and 6.")

# Results for each selection.
while True: 
    user_choice = get_user_choice()
    
    if user_choice == '1':
        # This is the cost of the plane ticket pp.
        city_flight = 100
        # Lets the user know we have their selection.
        print("Spain selected")
        print(f"Your flights will cost £{city_flight} per person")
        # Calculate the total cost relative to number of people.
        plane_cost = city_flight * num_of_people
        print(f"This comes to £{plane_cost} for everyone")
        break

    elif user_choice == '2':
        city_flight = 200
        print("Germany selected.")
        print(f"Your flights will cost £{city_flight} per person")
        plane_cost = city_flight * num_of_people
        print(f"This comes to £{plane_cost} for everyone")
        break

    elif user_choice == '3':
        city_flight = 300
        print("Portugal selected.")
        print(f"Your flights will cost £{city_flight} per person")
        plane_cost = city_flight * num_of_people
        print(f"This comes to £{plane_cost} for everyone")
        break

    elif user_choice == '4':
        city_flight = 400
        print("Greece selected.")
        print(f"Your flights will cost £{city_flight} per person")
        plane_cost = city_flight * num_of_people
        print(f"This comes to £{plane_cost} for everyone")
        break

    elif user_choice == '5':
        city_flight = 500
        print("France selected.")
        print(f"Your flights will cost £{city_flight} per person")
        plane_cost = city_flight * num_of_people
        print(f"This comes to £{plane_cost} for everyone")
        break

    # If the user selects to exit we break the loop.
    elif user_choice == '6':
        print("Exiting program.")
        break
    # If the user selects anything else we break the loop.
    else:
        print("An unexpected error occurred.")
        break


# Ask the user how many nights they are staying. Store as variable.
num_nights = int(input("How many nights do you want to stay?"))
# The hotel will be £300 per night.
# Work out the hotel cost by doing number of nights x nightly rate.
hotel_cost = num_nights * 300
# Work out a per person price by dividing hotel cost by amount of people.
hotel_pp = hotel_cost/num_of_people
print(f"Your hotel for {num_nights} nights will cost £{hotel_pp} per person")
print(f"This will be {hotel_cost} total")

# Ask the user how many days car rental they want. Store as variable.
rental_days = int(input("How many days car rental do you want?"))
# The rental daily cost is £100.
# Work out the rental cost by mulitplying rental days by daily cost.
car_rental = rental_days * 150
print(f"Your rental for {rental_days} days will cost £{car_rental}")

# Work out the total cost of the trip by adding flights, hotel and car charges.
holiday_cost = plane_cost + hotel_cost + car_rental
print(f"Your entire holiday will cost £{holiday_cost:.2f} for {num_of_people} of you.")
# Calculate a per person price by dividing the total cost by num people.
holiday_pp = holiday_cost / num_of_people
print(f"This would be £{holiday_pp:.2f} per person.")
