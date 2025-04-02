def count_and_say(n):
    def rec_count_and_say(n, string):
        if n == 1:
            return "1"
        string = rec_count_and_say(n - 1, string)

        string1 = ""
        n = 1
        letter = string[0]

        for i in range(1, len(string)):
            if letter == string[i]:
                n += 1
            else:
                string1 += str(n) + str(letter)
                letter = string[i]
                n = 1

        string1 += str(n) + str(letter)
        string = string1
        return string

    return rec_count_and_say(n, "")