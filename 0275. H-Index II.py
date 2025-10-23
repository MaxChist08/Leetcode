def h_index(citations):
    start = 0
    finish = len(citations) - 1

    while start <= finish:
        middle = (start + finish) // 2
        if len(citations) - middle > citations[middle]:
            start = middle + 1
        else:
            finish = middle - 1

    return len(citations) - start