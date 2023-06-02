def is_palindrome_iterative(word):
    if type(word) != str or len(word) == 0:
        return False
    word = word.lower()
    if word == word[::-1]:
        return True
    return False
    raise NotImplementedError
