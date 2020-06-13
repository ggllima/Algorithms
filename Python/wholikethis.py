"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, 
which must take in input array, containing the names of people who like an item. 
It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

"""

# first way, it is not the official answer, but in other circumstances it is functional

def likes(names=[]):
    if len(names) == 1:
        return print(names[0]+' like this')
    if len(names) == 2:
        return print(str(names[0])+' and '+names[1]+' like this')
    if len(names) > 0 and len(names) < 4:
        return print(str(names[0])+', '+str(names[1])+' and '+str(names[2]) + ' like this')
    if len(names) >= 4:
        final_len = len(names) - 2
        return print(str(names[0])+', '+str(names[1])+' and '+str(final_len) + ' others like this')
    if len(names) == 0:
        return print("no one likes this")

# second way, with official answer

def likes(names):
    if len(names) == 1:
        return names[0]+' likes this'
    if len(names) == 2:
        return names[0]+' and '+names[1]+' like this'
    if len(names) > 0 and len(names) < 4:
        return names[0]+', '+names[1]+' and '+names[2] + ' like this'
    if len(names) >= 4:
        final_len = len(names) - 2
        return names[0]+', '+names[1]+' and '+ str(final_len)+ ' others like this'
    if len(names) == 0:
        return "no one likes this"