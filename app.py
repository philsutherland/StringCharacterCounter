sentence = "Replace this text with your desired sentence!"

holder = {}

# Convert string to lowercase and replace leading/trailing spaces
sentence = sentence.strip()
sentence = sentence.lower()

# Count number of instances of each character
for character in sentence:
    if character in holder:
        holder[character] += 1
    else:
        holder[character] = 1

# Find the count of the most repeated letter(s)
top_letter_count = 1
for character in holder:
    if holder[character] > top_letter_count:
        top_letter_count = holder[character]

# Create a dictionary with the most repeated letter(s)
top_letters = {}
for character in holder:
    if holder[character] == top_letter_count:
        top_letters[character] = holder[character]

# Print the most repeated letter(s)
if len(top_letters) == 1:
    print("The most repeated letter is:")
else:
    print("The mose repeated letters are:")
print(top_letters)
