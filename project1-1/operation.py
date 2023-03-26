# addition 덧샘 연산
def add(left_value,right_value):
    # TODO
    return

# subtract 뺄샘 연산
def sub(left_value,right_value):
    # TODO
    return

# multiplied by 곱샘 연산
def mul(left_value,right_value):
    # TODO
    return

# divided by 나눗샘 연산
def div(left_value,right_value):
    # TODO
    return

# power 거듭제곱 연산
def power(left_value,right_value):
    # TODO
    return

# modulate 나머지 연산
def mod(left_value,right_value):
    # TODO
    return

# floor div 나머지 연산
def floor_div(left_value,right_value):
    # TODO
    return

operator_map = {
    '/' : div,
    '*': mul,
    '-': sub,
    '+': add,
    '^': power,
    '%': mod,
    '//': floor_div,
}

def binaryOperate(operand1,operand2,operator):
    result = operator_map[operator](operand1,operand2)
    return "" if result is None else str(result)