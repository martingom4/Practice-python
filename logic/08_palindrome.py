#tengo que hacer un programa que me diga si una palabra es un palindromo o no


def is_palindrome(word:str) -> bool:
    string = str(word)
    return string == string[::-1]

print(is_palindrome('ana'))
print(is_palindrome(121))
