#!/usr/bin/env python3


class Plant:
    name: str
    height: float
    _age: int
    growth: float

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30
    rose.growth = 0.8
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {rose.height - start_height:.1f}cm")
