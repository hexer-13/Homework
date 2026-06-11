def is_palindrome(phrase):
    check_phrase = "".join(char.lower() for char in phrase if char.isalnum())
    reversed_phrase = check_phrase[::-1]
    if check_phrase == reversed_phrase:
        print(phrase, "is a palindrome")
    else:
        print(phrase, "is not a palindrome")

is_palindrome(input("Enter a phrase: "))