def myAtoi(self, s):
        # Step 1: Ignore leading whitespaces
        s = s.lstrip()

        if not s:
            return 0

        # Step 2: Check for sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1

        # Step 3: Convert characters to integer
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # Step 4: Apply the sign
        result *= sign

        # Step 5: Clamp the result within the 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
