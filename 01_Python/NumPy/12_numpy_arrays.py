import numpy as np 
 
# Creating Numpy Arrays Using Lists

# One dimensional array
print("One dimensional array : ")
num1 = [1, 2, 3, 4]
arr1 = np.array(num1)
print(arr1)
print("Dimension of array : ",arr1.ndim)
print("Type of array : ",type(arr1))

# Two dimensional array
print("Two dimensional array : ")
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]
arr2 = np.array([num1, num2])
print(arr2)

# Two dimensional array
print("Two dimensional array : ")
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7, 8]
num3 = [9, 10, 11, 12]
arr3 = np.array([num1, num2, num3])
print(arr3)
print("Shape of 2D array : ",arr3.shape)

# Creating Text array
text1 = "Ashwini"
text2 = ["My", "name", "is", "Ashwini"]
arr4 = np.fromiter(text1, dtype="U1")
arr5 = np.fromiter(text2, dtype="U3")
arr6 = np.fromiter(text2, dtype="U7")
print("Single iterated array : ",arr4)
print("Array of Triple Characters : ",arr5)
print("Array of Multiple Characters : ",arr6)

# Creating Numpy Arrays Using Special Functions

# numpy.arange() function
arr7 = np.arange(1, 10, 1, dtype=int)
print("Array Using arange() function : ")
print(arr7)

# numpy.linspace() function
arr8 = np.linspace(0, 12, 6, dtype=float)  
print("Array Using linspace() function : ")
print(arr8)   

# numpy.empty() function
arr9 = np.empty((3, 2), dtype=float)
print("Array Using empty() function : ")
print(arr9)

# numpy.zeros() function 
print("Array Using zeros() function : ")
print(np.zeros((3, 3), dtype=int))

# numpy.ones() function
print("Array Using ones() function : ")
print(np.ones((3, 3), dtype=int))

# numpy.full() function
print("Array Using full() function : ")
print(np.full((3, 3), 5, dtype=float))      

# Creating array of random elements

# numpy.random.rand() function
print("Array of random numbers from 0 to 1 : ")
print(np.random.rand(2, 3))

# numpy.random.randn() function
print("Array of random numbers with normal distribution : ")
print(np.random.randn(2, 2))

# numpy.random.randint() function
print("Array of random integer numbers : ")
print(np.random.randint(1, 10, size=(2, 3)))

# Creating Numpy Arrays Using Matrix Creation Routines

# numpy.eye() function
print("Identity matrix : ")
print(np.eye(3, 2, dtype=int))

# numpy.diag() function
print(arr3)
print("Array of Main Diagonal elements : ")
print(np.diag(arr3))
print("Array of elements above Main Diagonal elements : ")
print(np.diag(arr3, 1))
print("Array of elements below Main Diagonal elements : ")
print(np.diag(arr3, -1))

# numpy.zeros_like() function
print(np.zeros_like(arr3, float, order="C"))

# numpy.ones_like() function
print(np.ones_like(arr3, int, order="F"))

# Numpy Array Indexing and Slicing

# Accessing Elements in 1D Arrays
print("Array is : ")
print(arr1)
print("Element from 1D Array : ",arr1[0])

# Accessing Elements in 2D Arrays
print("Array is : ")
print(arr2)
print("Element from 2D Array : ",arr2[0,2])     # Axis count starts from 0

# Accessing Elements in 3D Arrays
print("Array is : ")
arr9 = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])
print(arr9)
print("Element from 3D Array : ",arr9[1, 2, 0])              # Depth, row, column

# Accessing Group of Elements Using Slicing

# Slicing in 1D Arrays
arr10 = np.array([10, 20, 30, 40, 50, 60])
print("Array is : ")
print(arr10)
print("Accessing first 3 elements : ",arr10[:3])        # start:stop:step
print("Accessing last 3 elements : ",arr10[:-4:-1])

# Slicing in 2D Arrays
print("Array is : ")
print(arr3)
print("Sliced elements : \n",arr3[0:2, 1:3])

# Slicing in 3D Arrays
print("Array is : ")
print(arr9)
print("Sliced elements : \n",arr9[0:2, [1,2], [1,1]])           # depth, rows, columns
print("Sliced elements : \n",arr9[0:2, :2, :2])           # depth, rows, columns

# Boolean Indexing
print("Array is : \n",arr10)
print("Elements less than 30 are : ",(arr10[~(arr10>=30)]))          # Logical operators can also be used

# Fancy Indexing
print("Array is : \n",arr10)
indices = [0,3,1,4]
print("Elements at Indices 0,3,1,4 are : ",arr10[indices])

# Integer Array Indexing
print("Indiced elements as array : ",arr10[[0,3,1,4]])

# Ellipsis in Indexing
print("Array is : \n",arr9)
print("Accessing Elements using Ellipsis : ")
print(arr9[0:2, 1, ...])

# Using Numpy.newaxis to Add New Dimensions
print("Array is : \n", arr3)
print(arr3[::-1, np.newaxis])

# Modifying Array Elements
print("Array is : \n", arr1)
arr1[1:3] = 10
print("Modified Array is : \n",arr1)

# Reshaping NumPy Array

# 2D Array
print("Array is : \n",arr10)
reshape2d = arr10.reshape(2,3)
print("Reshaped Array : ")
print(reshape2d)

# 3D Array
arr11 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Array is : \n",arr11)
reshape3d = arr11.reshape(3,2,2)            # depth, rows, columns
print("Reshaped Array : ")
print(reshape3d)

# Automatic calculation on second dimension by Numpy by using (-1)
reshape_1 = arr11.reshape(3,-1)
print("Reshaped Array : ")
print(reshape_1)

# Resizing Numpy Arrray
arr12 = np.array([1, 2, 3, 4, 5, 6])
print("Array is : \n", arr12)
resize = np.resize(arr12 ,(3,4))
print("Resized Array : \n")
print(resize)

# Joining multiple arrays by creating a new axis in output
# Using numpy.stack() function
a = np.array([[[1, 2], [3, 4]],
             [[5, 6], [7, 8]]])
b = np.array([[[10, 20], [30, 40]],
             [[50, 60], [70, 80]]])
print("Arrays are : ")
print(a,"\n", b)
# 0=rows  1=columns -1=same as 1(Last dimension) 2,3= works with higher dimension data
print("Joined Array is : ")
new = np.stack((a, b), axis=2)        
print(new)

# Splitting Arrays
print("Array is : ")
arr12 = np.arange(12)
# Using numpy.split() function
sp = np.split(arr12, 4)
print("Splitted array using split() is : ")
print(sp)
# Using numpy.vsplit() function
vsp = np.vsplit(a, 2)
print("Splitted array using vsplit() is : ")
print(vsp)
# Using numpy.hsplit() function
hsp = np.hsplit(a, 2)
print("Splitted array using hsplit() is : ")
print(hsp)
# Using numpy.dsplit() function
print("Array is : ")
print(arr9)
dsp = np.dsplit(arr9, 3)
print("Splitted array using dsplit() is : ")
print(dsp)

# NumPy Broadcasting
# Broadcasting a scalar to a 1D Array
print("Array is : ")
res1 = a.reshape(2,4)
print(res1)
x = 100
print("Array Broadcastng to 100 : ")
print(res1 + x)
# Broadcasting 2 arrays
res2 = b.reshape(2,4)
print("Array Broadcasting two arrays : ")
print(res1 + res2)
# Broadcasting in Conditional operations using numpy.where()
arr13 = np.random.randint(1, 100, size = (1,8))
print("Array is : ")
print(arr13)
print("Broading Arrays using np.where() : ")
string = np.array(["Adult", "Minor"])
elegible = np.where(arr13 > 18, string[0], string[1])
print(elegible)

