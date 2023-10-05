# # my_array = [12, 33, 4, 231, 3, 22, 10]

# # upArray = sorted(my_array)
# # downArray = sorted(my_array, reverse=True)

# # loop = True

# # while loop == True:
# #     print(my_array)
# #     option = input("'up' or 'down'? ")
# #     if option == "up":
# #         print(upArray)
# #     elif option == "down":
# #         print(downArray)
# #     else:
# #         print("Invalid choice.")
# #         loop = False

# word = input("enter a string: ")

# doubledString = ""

# for char in word:
#     doubledString += char * 2

# print(doubledString)

string = "Apple"
new_list = []
string_list = sorted(list(string.lower()))
for char in string_list:
    
    if string_list[inc] == string_list[inc + 1]:
        print(f"{string} is not an isogram.")
    inc + 1