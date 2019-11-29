#search a text file for words with all vowels

ToOpen = input("enter a text file name:")
file = open(ToOpen,"r")
def Vowel_a(line):
    if 'a' in line:
        return True
def Vowel_e(line):
    if 'e' in line:
        return True
def Vowel_i(line):
    if 'i' in line:
        return True
def Vowel_o(line):
    if 'o' in line:
        return True
def Vowel_u(line):
    if 'u' in line:
        return True
def all_five_vowels(word):
    for line in word:
        if 'a' in line:
            if 'e' in line:
                if 'i' in line:
                    if 'o' in line:
                        if 'u' in line:
                            return True
                
        

if all_five_vowels(file) == True:
    print("This file contains a word(s) with all 5 vowels")
else:
    print("This file does not contain a word with all the vowels")
