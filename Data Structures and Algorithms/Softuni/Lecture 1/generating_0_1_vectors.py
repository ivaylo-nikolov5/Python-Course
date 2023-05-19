def generate_vectors(arr, idx):
    if idx >= len(arr):
        print(*arr, sep="")
        return
    for i in range(2):
        arr[idx] = i
        generate_vectors(arr, idx + 1)


a = int(input())
cells = [0] * a
generate_vectors(cells, 0)