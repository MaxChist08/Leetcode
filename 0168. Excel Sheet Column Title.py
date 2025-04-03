def convert_to_title(columnNumber):
    columnTitle = ""

    while columnNumber != 0:
        if columnNumber % 26 - 1 < 0:
            columnTitle = "Z" + columnTitle
            columnNumber = (columnNumber - columnNumber % 26) // 26 - 1
        else:
            columnTitle = chr(ord("A") + columnNumber % 26 - 1) + columnTitle
            columnNumber = (columnNumber - columnNumber % 26) // 26

    return columnTitle