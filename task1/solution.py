def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__

        for arg, (param_name, expected_type) in zip(args, annotations.items()):
            if param_name != 'return' and not isinstance(arg, expected_type):
                raise TypeError(
                    f"Argument '{param_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(arg).__name__}."
                )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
