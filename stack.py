def push(stack, ele):
    stack.append(ele)
    print(ele, "inserted into stack successfully")
 
def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
        return 
    print(stack[-1], "deleted successfully")
    stack.pop()