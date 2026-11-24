import re
def checkString(self, s: str) -> bool:
    return re.match(r"^a*b*$",s) != None