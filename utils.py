def highlight(func):
    def inner(*args, **kwargs):
        element = func(*args, **kwargs)
        parent = element._parent
        parent.execute_script("arguments[0].style.border='5px solid blue'", element)
        return element

    return inner


def highlights(func):
    def inner(*args, **kwargs):
        elements = func(*args, **kwargs)
        for element in elements:
            parent = element._parent
            parent.execute_script("arguments[0].style.border='5px solid blue'", element)
        return elements

    return inner
