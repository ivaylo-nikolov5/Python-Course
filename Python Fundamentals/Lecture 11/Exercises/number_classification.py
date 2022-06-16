def number_classification(numbers):
    positives = [x for x in numbers if int(x) >= 0]
    negatives = [x for x in numbers if int(x) < 0]
    evens = [x for x in numbers if int(x) % 2 == 0]
    odds = [x for x in numbers if int(x) % 2 != 0]

    print(f"Positive: {', '.join(positives)}")
    print(f"Negative: {', '.join(negatives)}")
    print(f"Even: {', '.join(evens)}")
    print(f"Odd: {', '.join(odds)}")


number_classification(numbers=input().split(", "))