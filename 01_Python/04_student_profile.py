#list = [23, "ashwini", 45 ]
#print(list)
#print(type(list))

# list2 = [1, 2, [5,7], [6.78,9.45], ["asd","ufg"], True ]
# print(list2)
#print(type(list2))
#print("index 0 = ",list2[0])
#rint("index 2 = ",list2[2])
#print("index 4 = ",list2[4])
#print("last index = ",list2[-1])
#print("list = ",list2[::1])
#print("Reversed list = ",list2[::-1])
#list2[2] = "Mango"
#print(list2)
# list2.append("Ashwini")
# print(list2)
# list2.remove(list2[3])
# print(list2)
#list2.append(list)
#print(list2)
# num = [i for i in range(0,25) if i%2==0]
# print(num)
# num = [[1,2],[3,4],[5,6]]
# #result = [item for i in num for item in i]

# for i in num:
#     for j in i:
#         print(j, end=" ")
n=5
for i in range(1,6):
    print("*"*i)
print()
for i in range(5,0,-1):
    print("*"*i)    
print()
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print((2*i - 1)*"*")    

fruits = ["Apple", "Banana", "Mango","Apple"]    
print(fruits.count("Apple"))
print(fruits.index("Apple"))

numbers = [1,2,3,4,5]
print(len(numbers))
