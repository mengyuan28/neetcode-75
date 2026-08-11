class MinStack:

    def __init__(self):
        self.min_stack = []
        self.main_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            latest_min = self.min_stack[-1]
            if val <= latest_min:
                self.min_stack.append(val)
        self.main_stack.append(val)

    def pop(self) -> None:
        cur_min = self.min_stack[-1]
        cur_val = self.main_stack[-1]
        if cur_val == cur_min:
            self.min_stack.pop()
        self.main_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return -1
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1
        
