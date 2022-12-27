# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

my_text = input('Введите текст: ')


def int_func(text):
    return text.capitalize()


print(int_func(my_text))
