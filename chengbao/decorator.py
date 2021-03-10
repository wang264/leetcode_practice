def print_input_out_put(func):
    def wrapper(*args, **kwargs):
        print("function name:  " + func.__name__ + "()")
        print(*args)
        print(**kwargs)
        func(*args, **kwargs)
        ret_val = func(*args, **kwargs)
        print(ret_val)

    return wrapper

#@print_input_out_put
def func_sum(a, b):
    return a + b


func_sum(1,2)

func_sum = print_input_out_put(func=func_sum)
