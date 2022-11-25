


class Foodtruck:
    def __init__ (self, name, staff, location, food):
        self.name = name
        self.staff = staff 
        self.location = location
        self.food = food 

    def __str__(self) -> str:
        return self.name
        
    """The diffrent things that is special about this food place"""
    def get_location(self):
        return f"{self.location}"
    def get_staff(self):
        return f"{self.staff}"
    def get_food(self):
        return f"{self.food}"
    def get_name(self):
        return f"{self.name}"

    """The things that is special for thus food place"""
foodtruck1 = Foodtruck("Funky chicken",3,"nacka","burgers")

def main():
    print(f"The foodtrucks name is {foodtruck1.get_name()} with {foodtruck1.get_staff()} in the staff. It is located in {foodtruck1.get_location()} and mainly coocks {foodtruck1.get_food()}.")

if __name__ == "__main__":
    main()