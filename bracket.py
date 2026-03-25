class Stack:
    def __init__(self, items=None):    
        if items is None:
            self.items = []
        else:
            self.items = items

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return None               
        return self.items.pop()       
    
    def is_empty(self):
        return len(self.items) == 0   

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]


def check_parenthesis(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.push(char)
            
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    
    return stack.is_empty()

print(check_parenthesis("((a+b) * [c-d])"))          
print(check_parenthesis("({[})"))                    
print(check_parenthesis("([)]"))                     
print(check_parenthesis("{[()()]}"))                 
print(check_parenthesis("((("))                      
print(check_parenthesis(")))"))                      