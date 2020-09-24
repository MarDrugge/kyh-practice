def compute_strength(pw):
    score = 0
    chars = set('#%&+_')

    if len(pw) > 10:
        score += 1
    if any(c.isalpha() for c in pw) and any(c.isdigit() for c in pw):
        score += 1
    #if not pw.isalnum(): # Kollar ALLA special-tecken
    #    score += 1
    if any((c in chars) for c in pw):
        score += 1

    if not any(c.isalpha() for c in pw) and not any(c.isdigit() for c in pw) and not any((c in chars) for c in pw):
        score == 0

    print(f'Ditt lösenord fick {score} av 3 poäng')
    return score


if __name__ == '__main__':
    compute_strength()
