# Write a program that allows a user to register students for an exam venue.
# First ask the user how many students are registering.
# Create a for loop that runs for that number of students.
# Each time the loop runs the program should ask the user to enter student ID.
# Write each student ID number to a text file called reg.form.txt
# Include a dotted line after each student ID.
# This doc will be used as an attendence registar.

# Open the file we are going to write to.
with open("reg_form.txt", "w") as file1:
    # Get the input from the user for how many students.
    num_students = int(input("How many students are registering?"))
    # Loop for the number of students.
    for _ in range(num_students):
        # Get the info off the user for student ID.
        student_ID = input("Please enter student ID")

        # Write this to the file with a new line after.
        file1.write(f"{student_ID}\n")

        # Writing a line of * after each ID so student can sign.
        file1.write("*******************\n")