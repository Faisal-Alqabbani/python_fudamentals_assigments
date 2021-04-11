# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(arr):
    for i,val in enumerate(arr):
        if val > 0:
            arr[i] = "big"    
    return arr


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += i
    arr[len(arr) - 1] = count
    return arr

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: x([6,3,-2]) should return 7 

def sum_total(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4

def length(arr):
    return len(arr)

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(arr):
    if len(arr) == 0:
        return False    
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(arr):
    analysis = {"sumTotal": 0, "average":0, "minimum":arr[0],"maximum":arr[0], "length":len(arr)}
    for i in arr:
        # get max value
        if i > analysis["maximum"]:
            analysis["maximum"] = i
        # get min valu
        elif i < analysis["maximum"]:
            analysis["maximum"] = i
        # get total sum
        analysis["sumTotal"] += i
    analysis["average"] = analysis["sumTotal"]/analysis["length"]
    return analysis


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(arr):
    return arr[::-1]
