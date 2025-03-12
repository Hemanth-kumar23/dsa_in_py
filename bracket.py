def checkParenthesis(mystr):
    open_list = ["(", "{", "["]
    close_list = [")", "}", "]"]
    stack = []
    
    for i in mystr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[-1]:
                stack.pop()
            else:
                return "Unbalanced"
    
    return "Balanced" if len(stack) == 0 else "Unbalanced"

# Test cases
string = "{[()]}"
print(string, "-", checkParenthesis(string))  # Balanced

string = "[{)}{}}(]"
print(string, "-", checkParenthesis(string))  # Unbalanced

string = "((()))"
print(string, "-", checkParenthesis(string))  # Balanced
