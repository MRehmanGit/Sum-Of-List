def sum_of_list(lst):
    # Initialize the total sum to 0
    total = 0
    # Iterate through each index in the list
    for everyElement in range(len(lst)):
        # Check if the current element is the last element in the list
        if(lst[everyElement] == len(lst)):
            # Print the current element followed by "=" (for the last element)
            print(lst[everyElement], "=", end=" ")
        else:
            # Print the current element followed by "+" (for all but the last element)
            print(lst[everyElement] , "+" , end=" ")
            # Add the current element to the total sum
        total += lst[everyElement]
    # Return the total sum of the elements in the list
    return total

# Testing the sum_of_list function with a sample list
my_list = [1,2,3,4,5,6,7,8,9,10]
print(sum_of_list(my_list))
