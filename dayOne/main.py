def replace_written_numbers(input_string):
    number_mapping = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }
    for written_number, digit in number_mapping.items():
        input_string = input_string.replace(written_number, digit)

    return input_string


def findDigits(DigitsAndNumbers):
    number_raw = []
    for element in DigitsAndNumbers:
        if element.isdigit():
            number_raw.append(element)
        else:
            pass
    contemporary = [number_raw[0], number_raw[-1]]
    number_clean = int("".join(contemporary))
    return number_clean


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    EachLine = []
    DigitArray = []
    sumOfAll = 0
    stringer = ""
    with open('listNumberDigits.txt') as f:
        [EachLine.append(line) for line in f.readlines()]

    for lines in EachLine:
        DigitArray.append(findDigits(replace_written_numbers(lines)))
    print(DigitArray.__len__())
    for i in DigitArray:
        print(sumOfAll.__str__() + "+" + i.__str__())
        sumOfAll = sumOfAll + i
        print(sumOfAll)

    print(sumOfAll)
