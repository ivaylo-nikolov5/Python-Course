def tagger(tag, text):
    return f"<{tag}>{text}</{tag}>"


def tags(tag):
    def decorator(function):
        def wrapper(*args):
            result = tagger(tag, function(*args))
            return result

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

