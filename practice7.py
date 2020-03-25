import functools


def name_and_args_decorator(func_to_decorate):
    def wrapper(*original_args, **original_kwargs):
        print(func_to_decorate.__name__)
        print(locals()['original_args'])
        print(locals()['original_kwargs'])
        return func_to_decorate(*original_args, **original_kwargs)
    return wrapper


@name_and_args_decorator
def square_function(n):
    return n**2


@name_and_args_decorator
def name_function(name, surename):
    return "imie:" + name + " nazwisko: " + surename


def main():
    print(square_function(3))
    print(name_function("Agnieszka", "Pas"))


if __name__ == "__main__":
    main()
