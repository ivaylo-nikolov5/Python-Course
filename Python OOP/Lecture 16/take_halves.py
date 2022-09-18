def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        while n > 0:
            result.append(next(seq))
            n -= 1
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
