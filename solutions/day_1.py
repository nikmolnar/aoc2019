class Solution:
    def solve_1(self, text):
        return sum(int(x)//3 - 2 for x in text.split('\n'))

    def solve_2(self, text):
        def fuel_mass(mass):
            fuel = mass//3 - 2

            if fuel < 1:
                return 0
            return fuel + fuel_mass(fuel)

        return sum(fuel_mass(int(x)) for x in text.split('\n'))
