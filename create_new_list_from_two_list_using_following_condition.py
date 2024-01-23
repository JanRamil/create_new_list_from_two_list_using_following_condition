# Create a new list from two list using the following condition
# Exercise 10

# Create pseudocode

# Create a code to present 
def merge_list(list1, list2):
    result_list = []
    
# Create code that will iterate the first list
    for num in list1:
        # Create a code that will check if it is odd
        if num % 2 != 0:
        # Create a code that will add the number to the new list
            result_list.append(num)

# Create code that will iterate the second list
    for num in list2:
        # Create a code that will check if it is even
        if num % 2 == 0:
            # Create a code that will add the number to the new list
            result_list.append(num)
            # Create a code that will return the result list
            return result_list
          
# Create code for the two given lists 
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


    