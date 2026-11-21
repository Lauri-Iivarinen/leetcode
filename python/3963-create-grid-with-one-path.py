class Solution:

    """
      just create path following edges since thats allowed
      ....
      ###.
      ###.
      ###.    
    """
  
    def createGrid(self, m: int, n: int) -> list[str]:
        first = "." * n
        last = "#" * (n - 1) + "."
        r = [first]
      
        for _ in range(m-1):
            r.append(last)
        
        return r
