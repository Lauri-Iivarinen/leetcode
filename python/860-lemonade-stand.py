def lemonadeChange(self, bills: list[int]) -> bool:
    available = {5: 0, 10: 0, 20: 0}
    for payment in bills:
        print(payment, available)
        p = payment
        payment -= 5
        tens = payment // 10
        payment -= 10 * tens
        fives = payment // 5
        
        available[p] += 1
        available[10] -= tens
        if available[10] < 0:
            available[10] += tens
            fives += 2 * tens
        available[5] -= fives
        if available[5] < 0:
            return False

    return True

print(lemonadeChange(None, [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))