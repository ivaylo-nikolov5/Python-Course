def array_sum(array_, idx):
    if idx == len(array_) - 1:
        return array_[idx]
    return array_[idx] + array_sum(array_, idx + 1)


array = [int(x) for x in input().split()]
print(array_sum(array, 0))
