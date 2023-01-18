def linear_search(seq, target):
    for i, obj in enumerate(seq):
        if obj == target:
            return i
