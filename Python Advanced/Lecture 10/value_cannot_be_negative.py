number = int(input())


class ValueCannotBeNegative(Exception):
    pass


while True:
    if not number:
        break

    if number < 0:
        raise ValueCannotBeNegative

    number = int(input())