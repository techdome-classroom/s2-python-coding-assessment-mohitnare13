class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        # Loop through each character in the string
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop the top element of the stack, if stack is not empty; otherwise, use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were properly matched
        return not stack

# Example usage
validator = Solution()
print(validator.isValid("()"))       
print(validator.isValid("()[]{}"))   
print(validator.isValid("(]"))       