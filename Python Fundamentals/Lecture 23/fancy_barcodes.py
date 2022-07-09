import re

lines = int(input())

pattern = r"(@#+)(([A-Z][a-zA-Z0-9]+)*[A-Z])(@#+)"

for x in range(lines):
    barcode = input()
    regex = re.match(pattern, barcode)
    if regex is None:
        print("Invalid barcode")
    else:
        code = regex.group(2)
        if len(code) < 6:
            print("Invalid barcode")
        else:
            is_digit = False
            number_code = ""
            for y in code:
                if y.isdigit():
                    is_digit = True
                    number_code += y

            if not is_digit:
                number_code = "00"

            print(f"Product group: {number_code}")