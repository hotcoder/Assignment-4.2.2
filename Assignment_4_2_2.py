'''
Created on Nov 20, 2017

@author: z002krv
'''
'''
Find Vowel or not
'''

vowelList = ["a","e","i","o","u"]

def isVowel(word):
    isVowel = False
    if(len(word) == 1):
        smallCaseWord  = word.lower()
        if(smallCaseWord in vowelList):
            isVowel= True 
    else:
        print("Please Enter String of length 1 only")
        return word+" Is not valid word"
    return isVowel

print(isVowel("a"))
print(isVowel("A"))
print(isVowel("Acadglid"))
print(isVowel("i"))
print(isVowel("b"))