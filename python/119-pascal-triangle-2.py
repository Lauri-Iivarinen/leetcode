def getRow(self, rowIndex: int) -> list[int]:
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    a = [1,1]
    for _ in range(rowIndex - 1):
        b = [1]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i+1])
        b.append(1)
        a = b
    return a