import functools


def function_call_count_decorator(func_to_decorate):
    @functools.wraps(func_to_decorate)
    def wrapper(*original_args, **original_kwargs):
        wrapper.num_calls += 1
        print(func_to_decorate.__name__ + ". calls: " + str(wrapper.num_calls))
        return func_to_decorate(*original_args, **original_kwargs)
    wrapper.num_calls = 0
    return wrapper


@function_call_count_decorator
def square_function(n):
    return n**2


@function_call_count_decorator
def name_function(name, surename):
    return "imie:" + name + " nazwisko: " + surename


def main():
    print(square_function(3))
    print(square_function(5))
    print(square_function(9))
    print(name_function("Agnieszka", "Pas"))
    print(name_function("Mister", "Nowak"))
    print(square_function(5))
    print(name_function("Ala", "Kowalska"))


if __name__ == "__main__":
    main()
