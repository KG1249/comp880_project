def add(x, y):
    return x + y

actual_result = add(3, 4)
expected_result = 7
assert (actual_result == expected_result)


def hello():
    return "hello world"


expected_result = hello()
assert (expected_result == "hello world")
