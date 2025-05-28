# Array Operations Processor

This project implements basic array operations in Python, such as finding the maximum and minimum values, calculating the average, and reversing the array. The program prompts the user to input integer values into an array and then performs various operations on that array. The results are printed to the console.

## Features

* **Find Maximum Value**: Determines the largest value in the array.
* **Find Minimum Value**: Determines the smallest value in the array.
* **Calculate Average**: Computes the average of the elements in the array.
* **Reverse Array**: Reverses the order of the elements in the array.

## Requirements

* Python 3.x or higher

## Usage

1. **Input Values**: The user is prompted to input five integers to populate an array.
2. **Array Operations**:

   * The program computes the maximum and minimum values of the array.
   * It calculates the average of the array values (using integer division).
   * It reverses the array.
3. **Display Results**: The program outputs:

   * Maximum value in the array
   * Minimum value in the array
   * Average value of the array
   * The reversed array

## Code Walkthrough

### 1. `findMax(arr)`

This function iterates through the array and finds the maximum value.

```python
def findMax(arr):
    max = arr[0]
    for i in range(1, 5):
        if arr[i] > max:
            max = arr[i]
    return max
```

### 2. `findMin(arr)`

This function iterates through the array and finds the minimum value.

```python
def findMin(arr):
    min = arr[0]
    for i in range(1, 5):
        if arr[i] < min:
            min = arr[i]
    return min
```

### 3. `calculateAverage(arr)`

This function calculates the average value of the array using integer division.

```python
def calculateAverage(arr):
    sum = 0
    average = 0
    for i in range(5):
        sum += arr[i]
    average = sum // 5
    return average
```

### 4. `reverseArray(arr)`

This function reverses the elements of the array in-place by swapping elements.

```python
def reverseArray(arr):
    temp = 0
    for i in range(3):  # Swaps elements from the start and end
        temp = arr[i]
        arr[i] = arr[5 - i - 1]
        arr[5 - i - 1] = temp
```

### 5. Main Program

The main part of the program initializes an array of size 5, collects user input, and calls the functions to perform array operations.

```python
integerArray = [0] * 5  # Create an array of size 5
for i in range(5):
    integerArray[i] = int(input("Enter value for element " + str(i+1) + ": "))

max = findMax(integerArray)
print("Maximum value in the array: " + str(max))

min = findMin(integerArray)
print("Minimum value in the array: " + str(min))

average = calculateAverage(integerArray)
print("Average value of the array: " + str(average))

reverseArray(integerArray)
print("Reversed array:")
for i in range(5):
    print(integerArray[i])
```

## Example Output

```
Enter value for element 1: 10
Enter value for element 2: 20
Enter value for element 3: 30
Enter value for element 4: 40
Enter value for element 5: 50

Maximum value in the array: 50
Minimum value in the array: 10
Average value of the array: 30
Reversed array:
50
40
30
20
10
```

## Notes

* The program assumes the user enters exactly five integers.
* The average calculation uses integer division (`//`), meaning the result is rounded down.
* The array reversal is done in place (modifying the original array).

## Future Enhancements

* Allow for dynamic input size (other than fixed size of 5).
* Add error handling for invalid inputs (e.g., non-integer inputs).
* Implement more array operations such as sorting, finding median, etc.

## License

This code is released under the MIT License. Feel free to modify and use it for your projects.
