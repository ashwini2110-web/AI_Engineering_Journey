# Printing Student's data using Nested Dictionary and list in dictionary

student = {
"student_1" : {
    "Name" : "Ashwini",
    "Age" : 20,
    "Engineering Branch" : "AIDS",
    "Subjects" : {"Digital Marketing":"Business","Artificial Intelligence":"Python","Data Science":"C language","Operating Systems":"Windows,Linus,MacOS"},
    "Career Goal" : ["AIDS Engineer","NLP Engineer","CV Engineer","GenAI Engineer"]
},
"student_2" : {
    "Name" : "Disha",
    "Age" : 18,
    "Engineering Branch" : "AIDS",
    "Subjects" : {"Digital Marketing":"Business","Artificial Intelligence":"Python","Data Science":"C language","Operating Systems":"Windows,Linus,MacOS"},
    "Career Goal" : ["AI Engineer","NLP Engineer","Entrepreuner","Content Creator"]
}
}
print(student)
print(type(student))

# Accessing Keys, Values and Items of a dictionary
print("Keys of dictionary are:")
print(student.keys())
print("Values of dictionary are:")
print(student.values())
print("Items of dictionary are:")
print(student.items())
print("Items of dictionary are:")

# Accessing single key, value and item of the dictionary
print(student["student_1"]["Name"])
print(student["student_2"]["Name"])