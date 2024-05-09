import time


def highlight(func):
    """
        Декоратор для добавления визуального выделения к элементам веб-страницы.

        :param func (function) - Функция для поиска элементов на веб-странице.
        Function: Функция, которая добавляет визуальное выделение к найденным элементам.
    """

    def inner(*args, **kwargs):
        """
               Внутренняя функция декоратора.

               Выполняет исходную функцию поиска элементов, затем добавляет к найденным
               элементам визуальное выделение путем применения стиля CSS.

               :param *args - Позиционные аргументы, переданные в исходную функцию.
               :param **kwargs - Именованные аргументы, переданные в исходную функцию.
        """
        element = func(*args, **kwargs)
        parent = element.parent
        parent.execute_script("arguments[0].style.border='5px solid blue'", element)
        time.sleep(0.2)
        parent.execute_script("arguments[0].style.border='none'", element)
        return element

    return inner


def highlights(func):
    """
        Декоратор для добавления визуального выделения к элементам веб-страницы.

        :param func (function) - Функция для поиска элементов на веб-странице.
        Function: Функция, которая добавляет визуальное выделение к найденным элементам.
    """

    def inner(*args, **kwargs):
        """
            Внутренняя функция декоратора.

            Выполняет исходную функцию поиска элементов, затем добавляет к найденным
            элементам визуальное выделение путем применения стиля CSS.

            :param *args - Позиционные аргументы, переданные в исходную функцию.
            :param **kwargs - Именованные аргументы, переданные в исходную функцию.
        """
        elements = func(*args, **kwargs)
        for element in elements:
            parent = element.parent
            parent.execute_script("arguments[0].style.border='5px solid blue'", element)
            time.sleep(0.2)
            parent.execute_script("arguments[0].style.border='none'", element)
        return elements

    return inner
