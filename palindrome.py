word = str (input("Enter a string to check it's a palindrome or not.\n"))
rvsword = word[::-1]
if word == rvsword:
    print ("{} word is palindrome".format(word))
else:
    print ("{} word is not palindrome".format(word))

