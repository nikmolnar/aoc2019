import copy


class Solution:
    def run_program(self, program, inputs, cur=0):
        program = copy.copy(program)

        output = None
        wait = False
        while cur < len(program):
            opcode = program[cur]

            if opcode == 99:
                break

            mode = [0, 0, 0]
            if opcode % 1000 // 100:
                mode[0] = 1
            if opcode % 10000 // 1000:
                mode[1] = 1
            if opcode % 100000 // 10000:
                mode[2] = 1

            opcode = opcode % 100

            if opcode == 1:
                p1, p2, p3 = program[cur + 1:cur + 4]

                if mode[0]:
                    left = p1
                else:
                    left = program[p1]

                if mode[1]:
                    right = p2
                else:
                    right = program[p2]

                program[p3] = left + right
                cur += 4
            elif opcode == 2:
                p1, p2, p3 = program[cur + 1:cur + 4]

                if mode[0]:
                    left = p1
                else:
                    left = program[p1]

                if mode[1]:
                    right = p2
                else:
                    right = program[p2]

                program[p3] = left * right
                cur += 4
            elif opcode == 3:
                p1 = program[cur + 1]
                try:
                    program[p1] = inputs.pop(0)
                except IndexError:
                    wait = True
                    break
                cur += 2
            elif opcode == 4:
                p1 = program[cur + 1]

                if mode[0]:
                    output = p1
                else:
                    output = program[p1]
                cur += 2
            elif opcode == 5:
                p1, p2 = program[cur+1:cur+3]

                if mode[0]:
                    jump = p1
                else:
                    jump = program[p1]

                if mode[1]:
                    loc = p2
                else:
                    loc = program[p2]

                if jump != 0:
                    cur = loc
                else:
                    cur += 3
            elif opcode == 6:
                p1, p2 = program[cur+1:cur+3]

                if mode[0]:
                    jump = p1
                else:
                    jump = program[p1]

                if mode[1]:
                    loc = p2
                else:
                    loc = program[p2]

                if jump == 0:
                    cur = loc
                else:
                    cur += 3
            elif opcode == 7:
                p1, p2, p3 = program[cur+1:cur+4]

                if mode[0]:
                    left = p1
                else:
                    left = program[p1]

                if mode[1]:
                    right = p2
                else:
                    right = program[p2]

                program[p3] = 1 if left < right else 0
                cur += 4
            elif opcode == 8:
                p1, p2, p3 = program[cur+1:cur+4]

                if mode[0]:
                    left = p1
                else:
                    left = program[p1]

                if mode[1]:
                    right = p2
                else:
                    right = program[p2]

                program[p3] = 1 if left == right else 0
                cur += 4

        return output, program, cur, wait

    def run_amplifier_sequence(self, program, sequence):
        value = 0
        for _ in range(5):
            value = self.run_program(program, [sequence.pop(0), value])[0]
        return value

    def find_permutations(self, low, high, exclude, places):
        if places < 1:
            return []

        permutations = []
        for i in (x for x in range(low, high) if x not in exclude):
            if places < 2:
                permutations += [[i]]
            else:
                permutations += [[i] + x for x in self.find_permutations(low, high, exclude + [i], places - 1)]

        return permutations

    def solve_1(self, text):
        program = [int(x) for x in text.split(',')]
        sequences = self.find_permutations(0, 5, [], 5)
        return max(self.run_amplifier_sequence(program, sequence) for sequence in sequences)

    def run_feedback_sequence(self, program, sequence):
        programs = [copy.copy(program) for _ in range(5)]
        cursors = [0] * 5
        value = 0
        first_loop = True
        while any(p is not None for p in programs):
            for i in range(5):
                if programs[i] is None:
                    continue

                if first_loop:
                    inputs = [sequence[i], value]
                else:
                    inputs = [value]

                value, program, cur, wait = self.run_program(programs[i], inputs, cur=cursors[i])

                cursors[i] = cur

                if wait:
                    programs[i] = program
                else:
                    programs[i] = None
            first_loop = False

        return value

    def solve_2(self, text):
        program = [int(x) for x in text.split(',')]
        sequences = self.find_permutations(5, 10, [], 5)
        return max(self.run_feedback_sequence(program, s) for s in sequences)
