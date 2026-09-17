import numpy as np

# Basic Arithmetic Operations 
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Array 1 : {a} \nArray 2 : {b}")
print(f"Addition : {a+b}")            # addition 
print(f"Subtraction : {a-b}")         # subtraction 
print("Multiplication : ",a*b)        # multiplication 
print("Division : ",a/b)              # division 
print("Modulus : ",a%b)               # modulus 
print("Power : ",a**b)                # power  
print("Floor division : ",b//a)       # floor division

# Arithmetic Operations using functions
print(f"Array 1 : {a} \nArray 2 : {b}")
print(f"Addition : {np.add(a, b)}")                                         # addition 
print(f"Subtraction : {np.subtract(a,b, dtype = float)}")    # subtraction 
print("Multiplication : ",np.multiply(a, b))                             # multiplication 
print("Division : ",np.divide(a,b))                                      # division 
print("Modulus : ",np.mod(a,b))                                          # modulus 
print("Power : ",np.power(b,a))                                          # power 

# Absolute value and sign
x = np.array([-3.5, 1.77, 0, -5.1])
print("Array is : ",x)
print(f"Absolute value of Array is : {np.abs(x)}")  # gives absolute value
print(f"Sign of Array is : {np.sign(x)}")           # gives signs 0, 1,-1
print(f"Square of Array is : {np.square(x)}")       # gives square
y = np.array([2,4,9])
print("Array is : ",y)
print(f"Exponent of Array is : {np.exp(y)}")        # gives Exponential value
print(f"Logarithmic of Array is : {np.log(y)}")     # gives logarithmic value 
print(f"Log to base 2 is : {np.log2(y)}")           # gives log to the base 2
print(f"Log to base 10 is : {np.log10(y)}")         # gives log to the base 10

# Trigonometric functions
angles = np.array([0, np.pi, np.pi/2], dtype = float)
print("Array is : ", (angles))
print(f"Sin of Array is : {np.sin(angles)}")
print(f"Cos of Array is : {np.cos(angles)}")
print(f"Tan of Array is : {np.tan(angles)}")
arc_values = np.array([0, 0.5, 1])
print("Array is : ", arc_values)
print(f"Arcsin of Array is : {np.arcsin(arc_values)}")
print(f"Arccos of Array is : {np.arccos(arc_values)}")
app = np.append(arc_values, np.inf)
print(f"Arctan of Array is : {np.arctan(app)}")
print("Hypotenuse of triangle with two sides(6,8) is : ", np.hypot(6,8))
      
# Rounding and Floor/ceil
print("Array is : ", x)
print("Nearest integer : ",np.round(x))                    # nearest integer
print("Lowest integer : ",np.floor(x))                     # lowest integer
print("Upper integer : ",np.ceil(x))                       # upper integer
print("Array with removed decimal part : ", np.trunc(x))   # removing decimal part

# Comparison Operations
p = np.array([1,2,3])
q = np.array([3,2,1])
print(f"Array 1 is : {p}\nArray 2 is : {q}")   # Comparison functions:
print("Equal : ", p == q)                      # np.equal()
print("Not Equal : ", p != q)                  # np.notequal()
print("Greater than : ", p > q)                # np.greater()
print("Less than : ", p < q)                   # np.less()
print("Greater than equal : ", p >= q)         # np.greater_equal()
print("Less than equal : ", p <= q)            # np.less_equal()

# Boolean Operations
r = np.array([False, True, False])
s = np.array([1, 0, 1])
print("Logical AND : ",np.logical_and(r, s))
print("Logical OR : ",np.logical_or(r, s))
print("Logical NOT : ",np.logical_not(r))
print("Logical XOR : ",np.logical_xor(r, s))

# Aggregation functions
arr = np.array([1,2,3,4,5])
print("Sum of elements : ",np.sum(arr))
print("Mean of elements : ",np.mean(arr))
print("Median of elements : ",np.median(arr))
print("Minimum of elements : ",np.min(arr))
print("Maximum of elements : ",np.max(arr))
print("Product of elements : ",np.prod(arr))
print("Standard deviation of elements : ",np.std(arr))       # Standard deviation
print("Variance of elements : ",np.var(arr))                 # variance
# Cumulative versions
print("Cumulative sum is : ",np.cumsum(arr))
print("Cumulative product is : ",np.cumprod(arr))

# Statistical Operations
l = np.array([10, 20, 30, 40, 50])
print("Array is : ", l)
print("Percentile out of 25 : ", np.percentile(l, 25))
print("Percentile out of 60 : ", np.percentile(l, 60))
print("Corrcoef of array is : \n", np.corrcoef([1,2,3], [2,4,6]))  # Correlation coefficient matrix

# Clip function
print("Clip function : ", np.clip(l,20,40))

# Linear Algebra Operations
A = np.array([[1,2], 
              [4,5]], dtype = float )
B = np.array([[10,11],
              [13,14]], dtype = float)
print("Array is : \n", A, "\nArray is : \n", B)
print("Multiplied matrix is : ")          # Matrix Multiplication other ways :
print(A.dot(B))                           # np.dot(A, B) and np.matmul(A, B)

print("Transpose is : \n", A.T)
print("Diterminant of matrix :\n",np.linalg.det(A))
print("Inverse of matrix :\n",np.linalg.inv(A))
print("Eigen Matrix : \n",np.linalg.eig(A))
print(np.linalg.norm(A))                                 


