def is_palindrome(s):
    s = s.lower()

    string_with_only_letters = ""

    for x in s:
        if (ord(x) >= ord("a")) and (ord(x) <= ord("z")) or ((ord(x) >= ord("0")) and (ord(x) <= ord("9"))):
            string_with_only_letters += x

    for i in range(0, len(string_with_only_letters) // 2):
        if string_with_only_letters[i] != string_with_only_letters[-i - 1]:
            return False

    return True