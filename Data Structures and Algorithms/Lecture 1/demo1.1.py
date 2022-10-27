def generate_vectors(arr, idx):
    if idx >= len(arr):
        print(*arr, sep="")
        return
    for x in range(2):
        arr[idx] = x
        generate_vectors(arr, idx + 1)


number = int(input())
array = [0] * number
generate_vectors(array, 0)