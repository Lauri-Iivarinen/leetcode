def generate(self, numRows: int) -> list[list[int]]:
        def add_row(r,i):
            if i <= 0:
                return r
            nr = [1]
            for j in range(len(r[-1])-1):
                nr.append(sum(r[-1][j:j+2]))
            nr.append(1)
            r.append(nr)
            return add_row(r, i - 1)

        if numRows == 1:
            return [[1]]
        return add_row([[1],[1,1]], numRows - 2)