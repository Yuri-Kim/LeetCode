class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = list(itertools.combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        self.index += 1
        return "".join(self.s[self.index - 1])

    def hasNext(self) -> bool:
        return self.index < len(self.s)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()