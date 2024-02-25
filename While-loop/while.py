# Run a programe that consistantly asks the user to enter a number
# When the user inputs -1 to programe should stop asking for another number
# We then need to calculate the average of the numbers entered, excluding -1
# Use the while loop to programme this

# Requesting the info from the user
number = int(input("Please enter any number:"))

# Starting place for our loop
num_of_inputs = 0
running_total = 0

# Whilst the imput is greater than 0 we add the imput to the running total
# As well as asking the user for another number
while number >= 0:
    num_of_inputs+=1
    running_total = running_total + number
    number = int(input(f"Total so far: {running_total}, another number:"))
# If the user input a number lower than 0 i.e -1
# We want to print the average of all the numbers they've input
# Without including the last number they entered
if number < 0:
    avg = running_total/num_of_inputs
    print(f"The average of all your numbers = {avg:.2}")
