print("=====================")
print("    Text Analyzer")
print("=====================")

name = input("Enter your name = ")

# Counting number of characters
def char():
    return len(name)    

# Counting number of words
def word():
    words = name.split(" ")
    return len(words)

# Counting number of vowels
def vowels():
    count = 0
    vowels = "aeiouAEIOU"
    for char in name:
        if char in vowels:
            count += 1
    return count        

# Uppercase and Lowecase
def upper():
    return name.upper()

def lower():
    return name.lower()

# Reversing the string
def reverse():
    return name[::-1]

# Calling the functions declared above

print(f"Number of characters: {char()}")
print(f"Number of words: {word()}")
print(f"Number of vowels: {vowels()}")
print(f"Uppercase: {upper()}")
print(f"Lowercase: {lower()}")
print(f"Reversed: {reverse()}")
   