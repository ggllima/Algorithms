"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

"""
# first way, not so practical, but functional
def disemvowel(string):
    str_list = [i for i in string]
    array_list = [i for i in str_list if i.lower() != 'a' and i.lower() != 'e' and i.lower() != 'i' and i.lower() != 'o' and i.lower() != 'u']
    string = ''.join(array_list)
    return string

# second way, a little more practical and very functional
def disemvowel(string):
    for i in 'aAeEiIoOuU':
        string = string.replace(i,'')
    return string

# third way, a mix of first and second way, it’s not necessary, but it’s fun

def disemvowel(string):
    str_list = [i for i in string]
    array_list = [i for i in str_list if i not in 'aAeEiIoOuU']
    string = ''.join(array_list)
    return string