'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return 0
    elif word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    elif word[0] != "t":
        return count_th(word[1:])  
    elif word[len(word) - 1]:
        return 1
          
    # Hate that I can't use the statement below.
    # It works.
    # return word.count("th")


    # TBC
    
