def h_index(citations):
    citations.sort()

    for i in range(0, len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i

    return citations[-1]