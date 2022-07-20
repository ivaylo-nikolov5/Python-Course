if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(reversed(sorted(arr)))
    arr = list(sorted(set(arr)))
    arr.remove(max(arr))
    print(arr[-1])


