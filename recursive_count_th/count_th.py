'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    found_th = 0


            

    if len(word) == 0:
        return 0
    elif word[0] == "t" and word[1] == "h":
        found_th += 1
        count_th(word[1:])
    else:
        count_th(word[1:])    

        
    return found_th
    # TBC
    
