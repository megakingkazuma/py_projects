# import inflect

# def number_to_words(number):
#     p = inflect.engine()
#     return p.number_to_words(number)

# number = 12345
# words = number_to_words(number)
# print(f"{number} in words: {words}")

# The inflect library simplifies converting numbers to words. You can install it using pip install inflect.


def number_to_words(number):
    units = ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand", "million", "billion", "trillion"]

    def helper(num, level):
        if num == 0:
            return ""
        elif num < 10:
            return units[num] + " "
        elif num < 20:
            return teens[num - 10] + " "
        elif num < 100:
            return tens[num // 10] + " " + helper(num % 10, level)
        else:
            return units[num // 100] + " hundred " + helper(num % 100, level)

    if number == 0:
        return "zero"

    result = ""
    level = 0
    while number > 0:
        chunk = number % 1000
        if chunk > 0:
            result = helper(chunk, level) + thousands[level] + " " + result
        number //= 1000
        level += 1

    return result.strip()


number = 12345
words = number_to_words(number)
print(f"{number} in words: {words}")
