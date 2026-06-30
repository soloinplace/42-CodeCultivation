#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float = 0.8,
    ) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.growth = growth
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.set_height(self._height + self.growth)

    def age(self) -> None:
        self.set_age(self._age + 1)


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()

    if rose.set_height(25.0):
        print(f"Height updated: {rose.get_height():.0f}cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")
    print()

    if rose.set_height(-10.0):
        print(f"Height updated: {rose.get_height():.0f}cm")
    else:
        print("Height update rejected")

    if rose.set_age(-25):
        print(f"Age updated: {rose.get_age()} days")
    else:
        print("Age update rejected")
    print()

    print("Current state:", end=" ")
    rose.show()
