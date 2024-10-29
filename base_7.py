def convertToBase7(self, num):
        # Use Python's built-in function to handle negative numbers
        if num == 0:
            return "0"
        
        # Determine the sign and convert the number to positive
        sign = '-' if num < 0 else ''
        num = abs(num)
        
        # Convert to base 7
        result = ''
        while num > 0:
            result = str(num % 7) + result
            num //= 7
        
        # Add the sign back if it was negative
        return sign + result
