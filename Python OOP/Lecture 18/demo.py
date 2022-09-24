def wrap_in_tags(tag, text):
    return f"<{tag}>{text}</{tag}>"

def tags(tag):
    def decorator(function):
        def wrapper(*args):
            return wrap_in_tags(tag, function(*args))

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
