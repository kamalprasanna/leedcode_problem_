class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def build(s: str, o: int, c: int) -> None:
            if c == 0:
                result.append(s)
                return
            if o > 0: build(s + "(", o - 1, c)
            if c > o: build(s + ")", o, c - 1) # more open than closed, so closing is safe
        build("", n, n)
        return result
