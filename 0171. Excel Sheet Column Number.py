def title_to_number(columnTitle):
    number = 0
    for i in range(len(columnTitle)):
        number += (ord(columnTitle[i]) - 64) * pow(26, len(columnTitle) - i - 1)
    return number