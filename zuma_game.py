# dynamic programming

def zuma_game(board, hand):
    # iterative
    result = 0
    dp = []
    for char in board: 
        # initial condition
        if not dp or dp[-1][0] != char:
            dp.append([char, 1])
            print("character is different than the last one")
            print(dp)
        else: 
            # check if character is the same as the last one in dp
            if (dp[-1][1] == 1) and (char in hand):
                print("character is the same as the last one and 2, and character is in hand")
                print(dp)
                dp.pop()
                result += 1
            else: 
                dp[-1][1] += 1
                print("character is the same as the last one but not 2")
                print(dp)
    if not dp and result > 0:
        return result
    else: 
        return -1

print(zuma_game("WRRBBW", "RB"))
print(zuma_game("WWRRBBWW", "WRBRW"))
print(zuma_game("G", "GGGGG"))