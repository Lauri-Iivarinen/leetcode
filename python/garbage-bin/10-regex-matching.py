#import re
def isMatch(self, s: str, p: str) -> bool:
    #return re.match(p,"^" + s + "$") != None # mby this is not the idea of the problem
    
    def proceed(s,p):
        print("proc, ", [s], [p])
        if len(s) == 0 or len(p) == 0:
            if len(p) == 2 and p[1] == "*":
                return True
            return len(s) == len(p)
        if len(p) > 1 and p[1] == "*":
            print("wildcard")
            if p[0] == ".":
                if len(p) == 2:
                    return True
                else:
                    a = ""
                    i = len(s) - 1
                    while i >= 0:
                        a = s[i] + a
                        if proceed(a, p[2:]):
                            return True
                        i -= 1
                    return False
            else:
               pass # WILDCARD IS SHIT
        elif s[0] == p[0] or p[0] == ".":
            return proceed(s[1:], p[1:]) 
        return False

    return proceed(s,p)




#print(isMatch(None, "aaabbb", "a*bbb"))
#print(isMatch(None, "bbba", "a*b*a"))

print(isMatch(None, "a", "a*a"))
#print()
#print(isMatch(None, "mississippi", "mis*is*p*."))


# ippi.   p*.


#print(isMatch(None, "bbbbba", ".*a*a"))
#print(isMatch(None, "aabb", ".*"))
#print(isMatch(None, "", ".*"))
#print(isMatch(None, "baabb", "b.*bba"))
