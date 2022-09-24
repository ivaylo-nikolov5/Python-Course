def wrap_in_tags(tag, text):
    return f"<{tag}>{text}</{tag}>"


def make_bold(function):
    def wrapper(*args):
        return wrap_in_tags("b", function(*args))

    return wrapper


def make_italic(function):
    def wrapper(*args):
        return wrap_in_tags("i", function(*args))

    return wrapper


def make_underline(function):
    def wrapper(*args):
        return wrap_in_tags("u", function(*args))

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
