print("=========================")
print("     Number Analyzer")
print("=========================")

numbers = list(map(int, input("Enter numbers separated by spaces : ").split()))
print(f"Numbers : {numbers}")

# Finding Repeating numbers and printing them in a list
repeat = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in repeat:
                repeat.append(numbers[i])
            break

print(f"Repeated numbers : {repeat}")

# Printing Even and Odd numbers from a given list

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]


print(f"Even numbers : {even_numbers} \nOdd numbers : {odd_numbers}")

# Finding frequency of the given list

frequency = {}
for number in numbers:
    if number not in frequency:
        frequency[number] = 1
    else:
        frequency[number] += 1
 
print(f"Frequency is : {frequency}")

# Returning prime numbers from a list 

def find_prime_numbers(numbers):
    prime = []
    for number in numbers:
        if number <= 1:
            continue
        is_prime_number = True
        for divisor in range(2,number):
            if number % divisor == 0:
                is_prime_number = False
                break
        if is_prime_number:
            prime.append(number)

    return prime
print(f"Prime numbers :  {find_prime_numbers(numbers)}")


# Printing factorial of a given number

# n = 5
# factorial = 1
# if n <= 1:
#     factorial = 1
# else:
#     for fact in range(n,0,-1):
#         factorial *= fact
# print(f"Factorial of {n} is : {factorial}")
