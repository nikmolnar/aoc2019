class Solution:
    def meets_criteria(self, password):
        password_s = str(password)

        if len(password_s) > 6:
            return False

        has_double = False
        for i in range(len(password_s) - 1):
            if password_s[i] > password_s[i+1]:  # yes, this works on digits-as-strings
                return False
            if password_s[i] == password_s[i+1]:
                has_double = True

        return has_double

    def meets_criteria_2(self, password):
        password_s = str(password)

        if len(password_s) > 6:
            return False

        has_double = False
        for i in range(len(password_s) - 1):
            if password_s[i] > password_s[i+1]:  # yes, this works on digits-as-strings
                return False
            if password_s[i] == password_s[i+1] and password_s.count(password_s[i]) < 3:
                has_double = True

        return has_double

    def solve_1(self, text):
        low, high = [int(x) for x in text.strip().split('-')]
        return [self.meets_criteria(x) for x in range(low, high + 1)].count(True)

    def solve_2(self, text):
        low, high = [int(x) for x in text.strip().split('-')]
        return [self.meets_criteria_2(x) for x in range(low, high + 1)].count(True)
