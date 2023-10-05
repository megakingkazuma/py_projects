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

# this one has the correct output but codewars doesnt accept it =(
    def Outlier(list):
    odd = 0
    even = 0
    odds = []
    evens = []
    for element in list:
        if element % 2 == 0:
            evens.append(element)
            even = even + 1
        else:
            odds.append(element)
            odd = odd + 1
    if odd < even:
        print(f"the only odd number: {odds}")
    else:
        print(f"the only even number: {evens}")


list1 = [160, 3, 1719, 19, 11, 13, -21]
Outlier(list1)

# this one checks if a strin is an isogram


def if_isogram(string):
    new_string = list(sorted(string.lower()))
    set_string = list(sorted(set(string.lower())))
    if set_string == new_string:
        print(f"{string} is an isogram.")
    else:
        print(f"{string} is not an isogram.")

if_isogram("aple")

# pin checker, pin must only have 4 or 6 digits and no letters or symbols must be included


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 4 and pin.isdigit():
        print("True")
    else:
        print("False")


validate_pin("aaaa1234")
