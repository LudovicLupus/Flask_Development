# python decorators

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)   # Create log file
    print("*** Printing via decorator function ***")

    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args} and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger    # Equivalent to display_info = my_logger(display_info) below
def display_info(name, age):
    print(f"Name: {name} - Age: {age}")


# display_info = my_logger(display_info)    # Does the same as "@my_logger" above
                                            # the original "display_info" function

display_info("Luis", 26)



