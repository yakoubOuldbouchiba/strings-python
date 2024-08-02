word= input("Please enter a word :")
word_revered = word[::-1]
print(word.upper())
print(word_revered.upper())
if word.upper().replace(' ' , '')  == word_revered.upper().replace(' ' , '') :
    print("It's a palindrome")
else :
    print("It's not a palindrome")

