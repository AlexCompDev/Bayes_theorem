# Функция для вычисления вероятности события A при условии B с использованием теоремы Байеса
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    global p_b
    # Вычисляем вероятность события не A
    not_a = 1 - p_a
    # Вычисляем вероятность события B
    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * not_a)
    # Вычисляем вероятность события A при условии B
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# Вводим входные данные с помощью функции input
p_b_description = str(input('Введите описание события: '))
p_a_description = str(input('Введите описание предшествующего (связанного) события: '))
p_a = float(input(f"Какова вероятность события - {p_a_description} в %: "))/100
p_b_given_a = float(input(f"Какова вероятность того, что {p_b_description} при наличии события ({p_a_description}) в %: "))/100
p_b_given_not_a = float(input(f"Какова вероятность того, что {p_b_description}, при отсутствии события ({p_a_description}) в %: "))/100

# Вычисляем результат с использованием теоремы Байеса
result = format(bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)*100, ".12f")

# Выводим результат с помощью функции print
print(f"Если {p_b_description} ({p_b*100}%), то вероятность того, что произошло событие ({p_a_description}) равна:", result, '%')
