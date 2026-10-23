# Jason Bhalla
# I pledge my honor that I have abided by the Stevens Honor System.

ones = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def number_to_words(number):
    if number == 100:
        return "one hundred"
    if number < 20:
        return ones[number]
    if number % 10 == 0:
        return tens[number // 10]
    return tens[number // 10] + "-" + ones[number % 10]


filename = input("Enter the text file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            parts = line.strip().split(maxsplit=1)

            if len(parts) != 2:
                print(f"Line {line_number}: INVALID - missing amount or description")
                continue

            amount, description = parts
            numbers = amount.split(".")

            if (len(numbers) != 2 or not numbers[0].isdigit() or not numbers[1].isdigit() or len(numbers[1]) != 2):
                print(f"Line {line_number}: INVALID - amount must have two decimal places")
                continue

            dollars = int(numbers[0])
            cents = int(numbers[1])

            if dollars > 100 or (dollars == 100 and cents > 0):
                print(f"Line {line_number}: INVALID - amount is over $100")
                continue

            if dollars == 1:
                dollar_unit = "dollar"
            else:
                dollar_unit = "dollars"

            if cents == 1:
                cent_unit = "cent"
            else:
                cent_unit = "cents"
            expected = ("only " + number_to_words(dollars) + " " + dollar_unit + " and " + number_to_words(cents) + " " + cent_unit)

            if " ".join(description.lower().split()) == expected:
                print(f"Line {line_number}: VALID - {amount}")
            else:
                print(f"Line {line_number}: INVALID - {amount}")
                print("  Expected:", expected)

except FileNotFoundError:
    print("File not found:", filename)
