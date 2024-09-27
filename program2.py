class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store the opening brackets
        stack = []
        # Mapping of closing brackets to opening brackets
        mapping = {')': '(', ']': '[', '}': '{'}
        
        # Iterate through the string
        for char in s:
            if char in mapping:
                # Get the top element from stack, or a dummy value if stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the mapped value of the current closing bracket doesn't match the stack's top element
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        # If stack is empty, all opening brackets are closed properly
        return not stack


# Unit test code
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))
    def test_mixed_parentheses(self):
        self.assertFalse(self.solution.isValid("(){"))

if _name_ == '_main_':
    unittest.main(argv=['first-arg-is-ignored'], 
    exit=False)