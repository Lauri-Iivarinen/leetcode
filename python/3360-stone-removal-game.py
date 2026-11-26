def canAliceWin(self, n: int) -> bool:
    bobs_turn = False
    amt = 10
    while True:
        n -= amt
        amt -= 1
        if amt < 0 or n < 0:
            break
        bobs_turn = not bobs_turn
    
    return bobs_turn