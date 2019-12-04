import sys
from importlib import import_module
from pathlib import Path


def load_input(day):
    input_file = Path(__file__).parent / 'inputs' / 'day_{}.txt'.format(day)
    with open(input_file, 'r') as f:
        return f.read().strip()


def solve_day(day):
    mod = import_module('solutions.day_{}'.format(day))
    input_text = load_input(day)
    solution = mod.Solution()

    print('Day {}'.format(day))

    print('  Part 1: {}'.format(solution.solve_1(input_text)))
    print('  Part 2: {}'.format(solution.solve_2(input_text)))


def main():
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        solve_day(day)
    else:
        for day in range(1, 32):
            try:
                solve_day(day)
            except ImportError:
                break




if __name__ == '__main__':
    main()
