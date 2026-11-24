def divide(self, dividend: int, divisor: int) -> int:
    def return_range(a, pos):
        if not pos:
            a = int("-" + str(a))
        if a > 2147483647:
            a = 2147483647
        if a < -2147483648:
            a = -2147483648
        return a

    #print(dividend, " / " ,divisor)
    
    a = ""
    d = str(dividend)
    pos = True
    if d[0] == "-":
        pos = not pos
        d = d[1:]
    if divisor < 0:
        pos = not pos
        divisor = int(str(divisor)[1:])

    if divisor == 1:
        return return_range(dividend, pos)

    
    carry = 0
    num = "0"
    for n in d:
        
        num += n
        sub = 0
        m = 0
        
        while m < int(num):
            sub += 1
            m += divisor

        a += str(sub)
        t_num = int(num)
        #print(sub)
        print(n, num, sub)
        
        while sub > 0:
            t_num -= divisor
            sub -= 1
        num = str(t_num)

    #num = int(num)
    #print(num)
    #num -= divisor
    r = 0
    #while num >= 0:
    #    r += 1
    #    num -= divisor

    a = int(a) + r
    

    return return_range(a, pos)
   
            
    



print(divide(None, 2147483647, 2))
#print(divide(None, 3, 2))
#print(divide(None, 0, 1))