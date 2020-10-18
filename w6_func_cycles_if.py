def plural_form(number, form1, form2, form3):
    """
    множественная форма числительных
    :param number: число
    :param form1: форма слова 1
    :param form2: форма слова 2
    :param form3: форма слова 3
    """
    second_digit = number % 100 // 10
    first_digit = number % 10
    rezult = ''
    if second_digit == 1 or first_digit > 4 or first_digit == 0:
        rezult = f"{number} {form3}"
    if second_digit != 1 and first_digit == 1:
        rezult = f"{number} {form1}"
    if (1 < first_digit < 5) and second_digit != 1:
        rezult = f"{number} {form2}"
    return rezult

def fizz_buzz():
    """Сумма чисел из диапазона от 1000 до 20000 включительно, которые делятся и на 3 и на 5"""
    summ_count = 0
    for i in range(1000, 20001):
        if i % 3 == 0 and i % 5 == 0:
            summ_count += i
    return summ_count

def fib_seq():
    """Последовательность Фибоначчи"""
    x1 = 1
    x2 = 1
    x3 = 0
    elements = 0
    even_elem_summ = 0
    even_elem = ''
    while x1 <= 10000000:
        if x3 < 10000000:
            x_prev = x1
        if x1 % 2 == 0:
            even_elem_summ += x1
            even_elem += str(x1)+' '
        x3 = x1 + x2
        x1, x2 = x2, x3
        elements += 1
    print(f"Количество элементов в последовательности: {elements}")
    print(f"Сумма всех четных элементов последовательности: {even_elem_summ}")
    print(f"Четные элемнеты последовательности: {even_elem}")
    print(f"Предпоследнее число последовательности: {x_prev}")


print(plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(fizz_buzz())
fib_seq()
