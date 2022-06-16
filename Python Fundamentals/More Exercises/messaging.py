def messaging(numbers, text):
    text = [x for x in text]
    message = ""
    counter = 0
    for x in range(len(numbers)):
        counter = 0
        for y in numbers[x]:
            for z in range(int(y)):
                counter += 1
                if counter == len(text):
                    counter = 0

        message += text[counter]
        text.pop(counter)

    print(message)


sequence_of_numbers = input().split(" ")
string = input()
messaging(sequence_of_numbers, string)