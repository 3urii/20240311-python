def check_parentheses(line):
    stack = []
    marks = []
    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
                marks.append(' ')  # 匹配的右括号，下方无标记
            else:
                marks.append('?')  # 不匹配的右括号，下方加问号
        else:
            marks.append(' ')  # 非括号字符，下方无标记
    # 添加不匹配的左括号标记
    marks.extend('x' for _ in stack)
    return marks


# 读取输入，直到EOF
try:
    while True:
        line = input("请输入一个字符串（或按Ctrl+D结束）：")
        marks = check_parentheses(line)

        # 打印原始字符串
        print(line)

        # 打印标记字符串，注意对齐
        print(''.join(marks).center(len(line), ' '))

except EOFError:
    pass