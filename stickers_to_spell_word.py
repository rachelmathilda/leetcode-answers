import math

def can_complete(stickers, word):
    for char in word:
        if not any(char in sticker for sticker in stickers):
            return False
    return True

def stickers_to_spell_word(stickers, word):
    if word == "":
        return 0
    elif can_complete(stickers, word):
        min_stickers = float("inf")
        # exhaustive search + backtracking
        for sticker in stickers:
            new_word = word
            for char in sticker: 
                new_word = new_word.replace(char, "", 1)
            
            if new_word == word:
                continue
                
            result = stickers_to_spell_word(stickers, new_word)

            if result != float("inf"):
                min_stickers = min(min_stickers, 1 + result)
            
        if min_stickers == float("inf"):
            return -1
        return min_stickers
    return -1
                
print(stickers_to_spell_word(["with", "example", "science"], "thehat"))
print(stickers_to_spell_word(["notice", "possible"], "basicbasic"))