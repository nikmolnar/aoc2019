class Solution:
    def run_program(self, text, input_value):
        program = [int(x) for x in text.split(',')]

        cur = 0
        output = None
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
                program[p1] = input_value
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

        return output

    def solve_1(self, text):
        return self.run_program(text, 1)

    def solve_2(self, text):
        return self.run_program(text, 5)
