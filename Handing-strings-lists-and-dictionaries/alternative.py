# Use a string of any words you choose.
# Creat a program which will change every other character to upper case. 
# And every other character to lower case. Eg "Hello World".
# Would be "HeLlO WoRlD"

string = "I've had a lovely sunday with my wife"
result = ""

# Using i as an unknow variable.
# If i is divisable by 2 will change character to upper case.
# If i is not divisable by 2 will change the character to lower case.
for i in range(len(string)):
    if not i % 2:
        result = result + string[i].upper()
    else:
        result = result + string[i].lower()

# Print the results
print(result)



# Now write a program that writes each word into upper and lower case.
# Split the string into a list of words.
list = string.split()
# We want to creat a string of every other word starting from 0.
upper_case = str(list[0::2])
# Now we have a string of all words we need to make capital letters.
words_up = upper_case.upper()
# We then split them back into a list of seperate words.
u_list = words_up.split()

# The same process as above but for lower words, starting from index 1.
# This means it will be the other alternate words.
lower_case = str(list[1::2])
words_low = lower_case.lower()
l_list = words_low.split()

# Create a string with the alternative words from each list we have now.
new_string = (f"{u_list[0]}{l_list[0]}{u_list[1]}{l_list[1]}{u_list[2]}{l_list[2]}{u_list[3]}{l_list[3]}")
# Removing any un-nessasary characters.
new_s = new_string.replace("'", " ").replace("[", "").replace("]", "").replace("," , "")
print(new_s)