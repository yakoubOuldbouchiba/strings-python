word1= input("Please enter a word :")
word1 = word1.replace(' ' , '')
word2= input("Please enter a word :")
word2 = word2.replace(' ' , '')
is_anagrams = True
if len(word1) != len(word1) :
    print("Not anagrams")
else:
    for char in word1 :
        if  word2.find(char) == -1 :
            is_anagrams = False
            break
    if is_anagrams:
        print("Anagrams")
    else :
        print("Not anagrams")