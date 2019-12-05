class Segment:
    def __init__(self, p1, p2, steps):
        self.p1 = p1
        self.p2 = p2
        self.steps = steps

    @property
    def is_vertical(self):
        return self.p1[1] == self.p2[1]

    @property
    def is_horizontal(self):
        return self.p1[0] == self.p2[0]

    def intersect(self, segment):
        if (self.is_vertical and segment.is_vertical) or (self.is_horizontal and segment.is_horizontal):
            return None

        intersection = (
            self.p1[0] if self.is_horizontal else segment.p1[0],
            self.p1[1] if self.is_vertical else segment.p1[1]
        )

        x = [self.p1[0], self.p2[0], segment.p1[0], segment.p2[0]]
        y = [self.p1[1], self.p2[1], segment.p1[1], segment.p2[1]]

        if (min(x) < intersection[0] < max(x)) and (min(y) < intersection[1] < max(y)):
            return intersection
        return None

    def steps_to(self, intersection):
        return self.steps - (abs(self.p2[0] - intersection[0]) + abs(self.p2[1] - intersection[1]))


class Solution:
    def get_wire_segments(self, wire):
        segments = []
        location = (0, 0)
        steps = 0

        for segment in wire.split(','):
            direction, length = segment[0], int(segment[1:])

            if direction == 'U':
                point = (location[0], location[1] + length)
            elif direction == 'R':
                point = (location[0] + length, location[1])
            elif direction == 'D':
                point = (location[0], location[1] - length)
            else:
                point = (location[0] - length, location[1])

            steps += length
            segments.append(Segment(location, point, steps))
            location = point

        return segments

    def get_distance(self, intersection):
        return abs(intersection[0]) + abs(intersection[1])

    def solve_1(self, text):
        wire_1, wire_2 = text.strip().split('\n')
        segments_1 = self.get_wire_segments(wire_1)
        segments_2 = self.get_wire_segments(wire_2)

        intersections = []
        for s in segments_1:
            intersections += [x for x in (s.intersect(x) for x in segments_2) if x]

        return min(self.get_distance(x) for x in intersections)

    def solve_2(self, text):
        wire_1, wire_2 = text.strip().split('\n')
        segments_1 = self.get_wire_segments(wire_1)
        segments_2 = self.get_wire_segments(wire_2)

        steps = []
        for s1 in segments_1:
            for s2 in segments_2:
                intersection = s1.intersect(s2)
                if intersection is not None:
                    steps.append(s1.steps_to(intersection) + s2.steps_to(intersection))

        return min(steps)
