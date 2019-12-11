import math


class Solution:
    def trace(self, grid, start, end):
        if end[1] == start[1]:  # Horizontal line
            return not any(grid[start[1]][x] for x in range(min(start[0], end[0]) + 1, max(start[0], end[0])))

        try:
            slope = (end[1] - start[1]) / (end[0] - start[0])
            b = start[1] - slope*start[0]
            y_fn = lambda x: slope*x + b
            return not any(
                grid[round(y_fn(x))][x]
                for x in range(min(start[0], end[0]) + 1, max(start[0], end[0]))
                if math.isclose(y_fn(x), round(y_fn(x)))
            )
        except ZeroDivisionError:  # Vertical line
            return not any(grid[y][start[0]] for y in range(min(start[1], end[1]) + 1, max(start[1], end[1])))

    def find_monitoring_station(self, grid, asteroids):
        return max(
            ((ast, [self.trace(grid, ast, t) for t in asteroids if t != ast].count(True)) for ast in asteroids),
            key=lambda x: x[1]
        )

    def solve_1(self, text):
        grid = [[True if x == '#' else False for x in row] for row in text.split('\n') if row.strip()]
        asteroids = [
            (x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x]
        ]
        return self.find_monitoring_station(grid, asteroids)[1]

    def solve_2(self, text):
        grid = [[True if x == '#' else False for x in row] for row in text.split('\n') if row.strip()]
        asteroids = [
            (x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x]
        ]
        station = self.find_monitoring_station(grid, asteroids)[0]

        destroyed = 0
        while True:
            will_destroy = [t for t in asteroids if t != station and self.trace(grid, station, t)]

            if destroyed + len(will_destroy) < 200:
                destroyed += len(will_destroy)
                for ast in will_destroy:
                    grid[ast[1]][ast[0]] = False
                    asteroids.remove(ast)
                continue

            will_destroy.sort(
                key=lambda x: (math.degrees(math.atan2(x[0] - station[0], station[1] - x[1])) + 360) % 360
            )
            target = will_destroy[200 - destroyed - 1]
            return target[0] * 100 + target[1]
