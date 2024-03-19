class Some:

    x: int = 5
    y: int = 2

    def __init__(self, a: float) -> None:
        self.a = a

    def add(self, a: int, b: int) -> int:
        return a + b

    @classmethod
    def sub(cls):
        return cls(13)


# instance = Some()
# Some.add = classmethod(Some.add)
# print(Some.add(2, 3))

print(Some.sub().__dict__)
