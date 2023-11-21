def accept_array_elements():
    # Accept array elements from the user
    n = int(input("Enter the number of elements in the array: "))
    array = []
    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)
    return array

def display_array_elements(array):
    # Display array elements
    print("Array elements:")
    for element in array:
        print(element, end=" ")
    print()

def find_sum_of_elements(array):
    # Find the sum of all array elements
    array_sum = sum(array)
    return array_sum

if __name__ == "__main__":
    # Accept and display array elements
    my_array = accept_array_elements()
    display_array_elements(my_array)

    # Find the sum of all array elements
    array_sum = find_sum_of_elements(my_array)
    print(f"Sum of array elements: {array_sum}")
