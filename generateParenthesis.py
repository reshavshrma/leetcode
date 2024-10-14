def generateParenthesis(self, n):
        result = []

        def backtrack(current, open_count, close_count):
            # If the current string is of length 2*n, it's a valid combination
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an open parenthesis, add it
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # If we can add a close parenthesis, add it
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        # Start the backtracking with an empty string and zero open/close parentheses
        backtrack("", 0, 0)
        return result
