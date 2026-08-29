print("===================\n"
"Student Profile\n"
"===================")

parameters = ["Name","Branch","Goal"]
student = []

with open("student.txt","w") as file:
    file.write("\n\n==Student Profile==\n\n")
    for info in parameters:
        answer = input(f"Enter your {info} = ")
        file.write(f"{info} : {answer}\n")
        student.append(answer)

with open("student.txt","r") as file:    
    data = file.read() 
    print(data)   

# print(parameters)
# print(student) 
# print(dict(zip(parameters,student)))  

