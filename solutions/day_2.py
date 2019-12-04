class Solution:
    def run_program(self, text, noun, verb):
        program = [int(x) for x in text.split(',')]

        # Initial state
        program[1] = noun
        program[2] = verb

        for cur in range(0, len(program), 4):
            opcode = program[cur]

            if opcode == 99:
                break

            p1, p2, p3 = program[cur + 1:cur + 4]
            left, right = program[p1], program[p2]

            if opcode == 1:
                program[p3] = left + right
            elif opcode == 2:
                program[p3] = left * right

        return program[0]

    def solve_1(self, text):
        return self.run_program(text, 12, 2)

    def solve_2(self, text):
        length = len(text.split(','))

        for noun in range(length):
            for verb in range(length):
                result = self.run_program(text, noun, verb)
                if result == 19690720:
                    return 100 * noun + verb
