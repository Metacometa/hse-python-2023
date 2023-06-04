import random
from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    # пиши код здесь
    return "Hello, " + name


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    # пиши код здесь
    return round(random.uniform(100, 1000000), 2)


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    # пиши код здесь
    result = True
    if phone_number[0] != '+':
        result = False
    elif phone_number[1] != '7':
        result = False
    else:
        for i in range(2, len(phone_number)):
            if phone_number[i] < '0' or phone_number[i] > '9':
                result = False
                break;

    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    # пиши код здесь
    return current_amount >= float(transfer_amount)


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    # пиши код здесь
    fixed_text = text[:]

    fixed_text = fixed_text.strip()
    fixed_text = ' '.join(fixed_text.split())

    fixed_text = fixed_text.replace('\'', '')
    fixed_text = fixed_text.replace('\"', '')

    fixed_text = fixed_text.capitalize()

    for word in uncultured_words:
        fixed_text = fixed_text.replace(word, len(word)*'#')
    return fixed_text


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:
    
    Иванов,Петр,Сергеевич,01.01.1991,10000
    
    Что должны вернуть на ее основе:
    
    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000
    
    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    user_edited_info = user_info[:]
    user_edited_info = user_edited_info.split(',')
    user_edited_info[0] = "Фамилия: " + user_edited_info[0]
    user_edited_info[1] = "Имя: " + user_edited_info[1]
    user_edited_info[2] = "Отчество: " + user_edited_info[2]
    user_edited_info[3] = "Дата рождения: " + user_edited_info[3]
    user_edited_info[4] = "Запрошенная сумма: " + user_edited_info[4]
    user_edited_info = '\n'.join(user_edited_info)

    return user_edited_info
