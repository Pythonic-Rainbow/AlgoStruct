def linear_search(seq, target):
    for i, obj in enumerate(seq):
        if obj == target:
            return i


def binary_search(seq, target):
    low, high = 0, len(seq)-1
    mid = (low+high) // 2
    while mid < high:
        if seq[mid] == target:
            return mid
        if seq[mid] < target:
            low = mid+1
        else:
            high = mid
        mid = (low+high) // 2
