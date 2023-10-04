# returning the difference between two arrays
def array_diff(list_a, list_b):
    result = []
    for element in list_a:
        if element not in list_b:
            result.append(element)
    for element in list_b:
        if element not in list_a:
            result.append(element)
    return result
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(list):
    result = []
    for element in list:
        if isinstance(element, int):
            result.append(element)
    return result