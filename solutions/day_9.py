import copy


class Solution:
    def ensure_memory(self, program, pointer):
        if len(program) <= pointer:
            program.extend([0] * (pointer - len(program) + 1))

    def run_program(self, program, inputs, cur=0):
        program = copy.copy(program)

        output = []
        wait = False
        rel_base = 0

        while cur < len(program):
            opcode = program[cur]

            if opcode == 99:
                break

            mode = [
                opcode % 1000 // 100,
                opcode % 10000 // 1000,
                opcode % 100000 // 10000
            ]

            opcode = opcode % 100

            if opcode == 1:
                p1, p2, p3 = program[cur + 1:cur + 4]

                if mode[0] == 1:
                    left = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    left = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    left = program[p1+rel_base]

                if mode[1] == 1:
                    right = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    right = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    right = program[p2+rel_base]

                if mode[2] == 0:
                    self.ensure_memory(program, p3)
                    program[p3] = left + right
                else:
                    self.ensure_memory(program, p3 + rel_base)
                    program[p3+rel_base] = left + right

                cur += 4
            elif opcode == 2:
                p1, p2, p3 = program[cur + 1:cur + 4]

                if mode[0] == 1:
                    left = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    left = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    left = program[p1+rel_base]

                if mode[1] == 1:
                    right = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    right = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    right = program[p2+rel_base]

                if mode[2] == 0:
                    self.ensure_memory(program, p3)
                    program[p3] = left * right
                else:
                    self.ensure_memory(program, p3 + rel_base)
                    program[p3+rel_base] = left * right

                cur += 4
            elif opcode == 3:
                p1 = program[cur + 1]
                try:
                    if mode[0] == 0:
                        self.ensure_memory(program, p1)
                        program[p1] = inputs.pop(0)
                    elif mode[0] == 2:
                        self.ensure_memory(program, p1 + rel_base)
                        program[p1+rel_base] = inputs.pop(0)
                except IndexError:
                    wait = True
                    break
                cur += 2
            elif opcode == 4:
                p1 = program[cur + 1]

                if mode[0] == 1:
                    output.append(p1)
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    output.append(program[p1])
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    output.append(program[p1+rel_base])
                cur += 2
            elif opcode == 5:
                p1, p2 = program[cur+1:cur+3]

                if mode[0] == 1:
                    jump = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    jump = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    jump = program[p1+rel_base]

                if mode[1] == 1:
                    loc = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    loc = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    loc = program[p2 + rel_base]

                if jump != 0:
                    cur = loc
                else:
                    cur += 3
            elif opcode == 6:
                p1, p2 = program[cur+1:cur+3]

                if mode[0] == 1:
                    jump = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    jump = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    jump = program[p1+rel_base]

                if mode[1] == 1:
                    loc = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    loc = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    loc = program[p2+rel_base]

                if jump == 0:
                    cur = loc
                else:
                    cur += 3
            elif opcode == 7:
                p1, p2, p3 = program[cur+1:cur+4]

                if mode[0] == 1:
                    left = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    left = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    left = program[p1+rel_base]

                if mode[1] == 1:
                    right = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    right = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    right = program[p2+rel_base]

                if mode[2] == 0:
                    self.ensure_memory(program, p3)
                    program[p3] = 1 if left < right else 0
                else:
                    self.ensure_memory(program, p3 + rel_base)
                    program[p3+rel_base] = 1 if left < right else 0

                cur += 4
            elif opcode == 8:
                p1, p2, p3 = program[cur+1:cur+4]

                if mode[0] == 1:
                    left = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    left = program[p1]
                else:
                    self.ensure_memory(program, p1 + rel_base)
                    left = program[p1+rel_base]

                if mode[1] == 1:
                    right = p2
                elif mode[1] == 0:
                    self.ensure_memory(program, p2)
                    right = program[p2]
                else:
                    self.ensure_memory(program, p2 + rel_base)
                    right = program[p2 + rel_base]

                if mode[2] == 0:
                    self.ensure_memory(program, p3)
                    program[p3] = 1 if left == right else 0
                else:
                    self.ensure_memory(program, p3 + rel_base)
                    program[p3+rel_base] = 1 if left == right else 0

                cur += 4
            elif opcode == 9:
                p1 = program[cur+1]

                if mode[0] == 1:
                    mod = p1
                elif mode[0] == 0:
                    self.ensure_memory(program, p1)
                    mod = program[p1]
                else:
                    self.ensure_memory(program, rel_base + p1)
                    mod = program[rel_base+p1]

                rel_base += mod
                cur += 2

        return output, program, cur, wait

    def solve_1(self, text):
        program = [int(x) for x in text.split(',')]
        outputs, *_ = self.run_program(program, [1])
        return outputs

    def solve_2(self, text):
        program = [int(x) for x in text.split(',')]
        outputs, *_ = self.run_program(program, [2])
        return outputs[0]
