# exhaustive search backtracking 

def can_complete(stickers, word):
    for char in word:
        if not any(char in sticker for sticker in stickers):
            return False
    return True

def stickers_to_spell_word(stickers, word):
    if can_complete(stickers, word):
        min_stickers = 0 
        # exhaustive search
        for sticker in stickers:
            for char in sticker: 
                if char in word:
                    # make choice
                    word = word.replace(char, "", 1)
                    # backtrack
                    if min_stickers < 1 + stickers_to_spell_word(stickers, word):
                        # undo choice
                        word = word + char
                        return min_stickers
                    else: 
                        return 1 + stickers_to_spell_word(stickers, word)
                else:
                    continue
    else: 
        return 0
    return min_stickers
                
print(stickers_to_spell_word(["with", "example", "science"], "thehat"))
print(stickers_to_spell_word(["notice", "possible"], "basicbasic"))