'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    letter_t = "t"
    found_th = 0
    got_th = []

    def find_th(new_str):
        if new_str[0] == letter_t:
            return got_th.append(new_str[:2])

    if len(word) == 0:
        return 0
    else: 
        find_th(word[1:])
        
    # TBC
    
