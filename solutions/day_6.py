class Orbit:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

class Solution:
    def count_orbits(self, orbit):
        if orbit.parent is None:
            return 0

        return 1 + self.count_orbits(orbit.parent)

    def build_orbit_map(self, text):
        orbit_data = [x for x in text.split('\n') if x.strip()]
        orbits = {'COM': Orbit('COM', None)}

        for orbit in orbit_data:
            direct, obj = orbit.split(')')
            parent = orbits.get(direct, Orbit(direct, None))
            orbits[direct] = parent
            if obj in orbits:
                orbits[obj].parent = parent
            else:
                orbits[obj] = Orbit(obj, parent)

        return orbits

    def solve_1(self, text):
        orbits = self.build_orbit_map(text)

        return sum(self.count_orbits(orbit) for orbit in orbits.values())

    def find_parents(self, orbit):
        if orbit.parent is None:
            return []

        return [orbit.parent] + self.find_parents(orbit.parent)

    def find_common_parent(self, orbit_1, orbit_2):
        parents_1 = self.find_parents(orbit_1)
        parents_2 = self.find_parents(orbit_2)

        for parent in parents_1:
            if parent in parents_2:
                return parent

    def count_transfers_to_parent(self, orbit, parent):
        if orbit.parent == parent:
            return 0

        return 1 + self.count_transfers_to_parent(orbit.parent, parent)

    def solve_2(self, text):
        orbits = self.build_orbit_map(text)
        parent = self.find_common_parent(orbits['YOU'], orbits['SAN'])
        print(parent.name)

        return (
            self.count_transfers_to_parent(orbits['YOU'], parent) +
            self.count_transfers_to_parent(orbits['SAN'], parent)
       )
