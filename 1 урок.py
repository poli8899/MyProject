#строчка палиндром или нет
def is_palindrome(s):
    return s == s[::-1] #берем всю строчку + шаг сравние строчку с перевернутой
print(is_palindrome('топот')) 