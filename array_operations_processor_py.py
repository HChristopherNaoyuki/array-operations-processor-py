# Project: Array Operations Processor

# Function definitions
def findMax(arr):
    # Declarations 
    max = arr[0]
    
    for i in range(1, 5):
        if arr[i] > max:
            max = arr[i]
    return max

def findMin(arr):
    # Declarations 
    min = arr[0]
    
    for i in range(1, 5):
        if arr[i] < min:
            min = arr[i]
    return min

def calculateAverage(arr):
    # Declarations 
    sum = 0
    average = 0
    
    for i in range(5):
        sum = sum + arr[i]
    average = sum // 5
    return average

def reverseArray(arr):
    # Declarations 
    temp = 0
    
    for i in range(3):  # 1 to 3 in pseudocode becomes 0 to 2 in Python
        temp = arr[i]
        arr[i] = arr[5 - i - 1]  # 6-i becomes 5-i in 0-based indexing
        arr[5 - i - 1] = temp

# Start

    # Declare an array of integers with a size of 5 
integerArray = [0] * 5
sum = 0
max = 0
min = 0
average = 0

    # Input values into the array using a loop 
for i in range(5):
    integerArray[i] = int(input("Enter value for element " + str(i+1) + ": "))

    # Call the findMax method 
max = findMax(integerArray)
print("Maximum value in the array: " + str(max))

    # Call the findMin method 
min = findMin(integerArray)
print("Minimum value in the array: " + str(min))

    # Call the calculateAverage method 
average = calculateAverage(integerArray)
print("Average value of the array: " + str(average))

    # Call the reverseArray method 
reverseArray(integerArray)
print("Reversed array:")
for i in range(5):
    print(integerArray[i])

# Stop