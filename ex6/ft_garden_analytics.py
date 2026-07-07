#!/usr/bin/env python3


class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls_number: int = 0
            self._age_calls_number: int = 0
            self._show_calls_number: int = 0

        def get_grow(self) -> int:
            return self._grow_calls_number

        def get_age(self) -> int:
            return self._age_calls_number

        def get_show(self) -> int:
            return self._show_calls_number

        def add_grow(self) -> None:
            self._grow_calls_number += 1

        def add_age(self) -> None:
            self._age_calls_number += 1

        def add_show(self) -> None:
            self._show_calls_number += 1

        def display(self) -> None:
            print(
                f"Stats: {self.get_grow()} grow, "
                f"{self.get_age()} age, "
                f"{self.get_show()} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth: float = 0.8,
    ) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self.growth: float = growth
        self._statistics: Plant.Statistics = self.Statistics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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
        self._statistics.add_show()
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._statistics.add_grow()
        self.set_height(self._height + self.growth)

    def age(self) -> None:
        self._statistics.add_age()
        self.set_age(self._age + 1)

    def get_statistics(self) -> "Plant.Statistics":
        return self._statistics

    def show_extra_statistics(self) -> None:
        return


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.color: str = color
        self.has_bloomed: bool = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
        growth: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls_number: int = 0

    def produce_shade(self) -> None:
        self._shade_calls_number += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.get_height():.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show_extra_statistics(self) -> None:
        print(f"{self._shade_calls_number} shade")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        growth: float = 2.1,
    ) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = 0.0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:.0f}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth: float = 0.8,
    ) -> None:
        super().__init__(name, height, age, color, growth)
        self.seeds: int = 0

    def age(self) -> None:
        self._statistics.add_age()
        self.set_age(self._age + 20)

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.get_statistics().display()
    plant.show_extra_statistics()


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 30.0)
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        f"Is 30 days more than a year?  "
        f"-> {Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year?  "
        f"-> {Plant.is_older_than_year(400)}"
    )
    print()

    print("=== Flower")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print("=== Tree")
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)
