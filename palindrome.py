word = str (input("Enter a word to test palindrome \n"))
rvsword = word[::-1]
if word == rvsword:
    print ("{} word is palindrome".format(word))
else:
    print ("{} word is not palindrome".format(word))

