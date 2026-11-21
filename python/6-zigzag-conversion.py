def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        r = ["" for _ in range(len(s))]
        grid = [r[:] for _ in range(numRows)]

        i,j = 0,0

        down = True
        for c in s:
            # print(down, i, j, c)
            grid[i][j] = c
            if down:
                i += 1
                if i >= len(grid):
                    i -= 2
                    if i < 0:
                        i = 0
                    j += 1
                    down = False
            else:
                i -= 1
                j += 1
                if i < 0:
                    i += 2
                    j -= 1
                    down = True
        
        a = ""
        for r in grid:
            # print(r)
            a += "".join(r)
        return a
