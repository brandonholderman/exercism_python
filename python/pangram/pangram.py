def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase = phrase.lower()
    return not (set(alphabet) - set(phrase))
    raise Exception('Not a Pangram!')
