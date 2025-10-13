def get_hint(secret, guess):
    A = 0

    mask = [0] * len(secret)

    for i in range(0, len(secret)):
        if secret[i] == guess[i]:
            A += 1
            mask[i] = 1

    secret_dict = dict()
    guess_dict = dict()

    for i in range(0, len(secret)):
        if mask[i] == 0:
            if secret[i] in secret_dict:
                secret_dict[secret[i]] += 1
            else:
                secret_dict[secret[i]] = 1

    for i in range(0, len(guess)):
        if mask[i] == 0:
            if guess[i] in guess_dict:
                guess_dict[guess[i]] += 1
            else:
                guess_dict[guess[i]] = 1

    B = 0
    for i in guess_dict:
        if i in secret_dict:
            B += min(guess_dict[i], secret_dict[i])

    return str(A) + 'A' + str(B) + 'B'