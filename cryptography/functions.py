import pandas as pd


def euclid_simple(a, b):
    """
    Простой алгоритм Евклида
    """
    # Инициализация списка для вывода результата
    result = list()

    # Инициализация констант
    a_constant = a
    b_constant = b

    # Реализация простая версия алгоритма Евклида
    while b != 0:
        result.append(f"{a} % {b} = {a % b}")
        a, b = b, a % b

    # Формирование результата
    result.append("")
    result.append(f"НОД({a_constant}, {b_constant}) = {a}")

    # Форматирование результата
    result = f"\nВычисления:\n{'\n'.join(result)}"

    print(result)

    return a


def euclid_extended(a, b):
    """
    Расширенный алгоритм Евклида
    """
    # Инициализация списка для вывода результата
    result = list()

    # Инициализация констант
    a_const = a
    b_const = b

    # Инициализация списка для коэффициентов
    cf_list = list()

    # Инициализация начальных значений для коэффициентов
    x2, x1 = 1, 0
    y2, y1 = 0, 1
    x, y = "-", "-"
    q, r = "-", "-"
    iteration = 1

    result.append("Итерация: 0")
    result.append(
        f"q = {q}, r = {r}, x = {x}, y = {y}, a = {a}, b = {b}, x2 = {x2}, x1 = {x1}, y2 = {y2}, y1 = {y1}"
    )
    result.append("")

    # Расширенная версия алгоритма Евклида
    while b != 0:

        # Добавление номера итерации в список
        result.append(f"Итерация: {iteration}")
        iteration += 1

        # Добавление коэффициентов в список
        cf_list.append([q, r, x, y, a, b, x2, x1, y2, y1])

        # Вычисление частного
        result.append(f"q = a // b = {a} / {b} = {a // b}")
        q = a // b

        # Вычисление остатка
        result.append(f"r = a mod b = {a} mod {b} = {a % b}")
        r = a % b

        # Обновление переменных
        result.append(f"a = b = {b}, b = r = {r}")
        a, b = b, r

        # Вычисление нового коэффициента x
        result.append(f"x = x2 - q * x1 = {x2} - {q} * {x1} = {x2 - q * x1}")
        x = x2 - q * x1

        # Вычисление нового коэффициента y
        result.append(f"y = y2 - q * y1 = {y2} - {q} * {y1} = {y2 - q * y1}")
        y = y2 - q * y1

        # Обновление промежуточных коэффициентов
        result.append(f"x2 = x1 = {x1}, x1 = x = {x}, y2 = y1 = {y1}, y1 = y = {y}")
        x2, x1 = x1, x
        y2, y1 = y1, y

        # Заглушка для разделения итераций
        result.append("")

    # Добавление финальных значений в список
    cf_list.append([q, r, x, y, a, b, x2, x1, y2, y1])

    # Создание датафрейма
    df = pd.DataFrame(
        cf_list, columns=["q", "r", "x", "y", "a", "b", "x2", "x1", "y2", "y1"]
    )

    # Формирование результата
    result.append(f"НОД({a_const}, {b_const}) = {a}")
    result.append(f"Коэффициенты: x = {x2}, y = {y2}")
    result.append(
        f"Целочисленная линейная комбинация: {x2} * {a_const} + {y2} * {b_const} = {x2 *a_const + y2 * b_const}"
    )

    # Форматирование результата
    result = f"\nТаблица коэффициентов:\n{df}\n\n{'\n'.join(result)}"

    print(result)

    return q, r, x, y, a, b, x2, x1, y2, y1


def comparison_one(a, b, m):
    """
    Решение сравнений первой степени с одним неизвестным
    """
    # Инициализация списка для вывода результата
    result = list()

    # Используем расширенный алгоритм Евклида для нахождения НОД(a, m)
    # gcd = НОД(a, m)
    _, _, _, _, gcd, _, x2, _, _, _ = euclid_extended(a, m)

    # Случай 1: НОД(a, m) = 1
    if gcd == 1:
        x0 = (x2 * b) % m
        result.append("")
        result = f"Решение сравнения {a}x = {b} (mod {m}): x ≡ {x0} (mod {m})"
        print(result)
        return result

    # Случай 2: НОД(a, m) = d > 1 и d не делит b
    elif b % gcd != 0:
        result.append("")
        result = "Решение не существует, так как b не делится на НОД(a, m)"
        print(result)
        return result

    # Случай 3: НОД(a, m) = d > 1 и d делит b
    elif b % gcd == 0:
        b_reduced = b // gcd
        m_reduced = m // gcd

        # Находим частное решение для сокращенного сравнения
        x0 = (x2 * b_reduced) % m_reduced

        # Формируем все d решений
        solutions = list()
        for counter in range(gcd):
            result.append(
                f"(x0 + {counter} * (b // НОД(a, m))) mod m = ({x0} + {counter} * ({b} // НОД({a}, {m}))) mod {m} = {(x0 + counter * m_reduced) % m}"
            )
            solutions.append((x0 + counter * m_reduced) % m)

        # Формирование результата
        result.append("")
        result.append(f"Решение сравнения {a}x = {b} (mod {m})")
        result.append(f"Множество решений: {solutions} (mod {m})")
        result.append(
            f"Эти решения образуют один класс вычетов по модулю m // НОД(a, m) = {m} // {gcd} = {m_reduced}"
        )

        # Форматирование результата
        result = f"\n{'\n'.join(result)}"

        print(result)

        return result

    else:
        raise Exception("Что-то пошло не так...")


def comparison_systems(equations):
    """
    Решение СИСТЕМ сравнений первой степени с одним неизвестным
    """
    # Инициализация списка для вывода результата
    result = list()

    # Вычисления значения вспомогательной переменной
    N = 1
    for equation in equations:
        N *= equation["m"]

    # Вычисление искомого значения
    a = 0
    for equation in equations:
        equation["N"] = N // equation["m"]
        _, _, _, _, _, _, x2, _, _, _ = euclid_extended(
            a=equation["N"], b=equation["m"]
        )
        a += equation["b"] * x2 * equation["N"]
        equation["N_output"] = f"N // m = {N} // {equation['m']} = {N // equation['m']}"
        equation["a_output"] = (
            f"{equation['b']} * {x2} * {equation['N']} = {equation['b'] * x2 * equation['N']}"
        )

    # Формирование результата для вспомогательных переменных
    result.append("")
    result.append("Вычисление значения вспомогательных переменных:")
    result.append(f"N = {N}")
    result += [
        f"N{counter + 1} = {equations[counter]['N_output']}"
        for counter in range(len(equations))
    ]

    # Формирование результата для искомого значения
    result.append("")
    result.append("Вычисление искомого значения:")
    result += [
        f"a{counter + 1} = {equations[counter]['a_output']}"
        for counter in range(len(equations))
    ]
    result.append(f"a = {a}")

    # Проверка результата
    result.append("")
    result.append("Проверка результата:")
    for equation in equations:
        equation_check = f"{a} (mod {equation['m']}) = {a % equation['m']}"
        if a % equation["m"] == equation["b"]:
            result.append(f"{equation_check} OK")
        elif a % equation["m"] != equation["b"]:
            result.append(f"{equation_check} ERROR")
        else:
            raise Exception("Что-то пошло не так...")

    # Форматирование результата
    result = "\n".join(result)

    print(result)

    return result


def legendre_symbol(number, prime):
    """
    Вычисление символа Лежандра

    :param number: Целое число, для которого вычисляется символ Лежандра.
    :param prime: Нечётное простое число, по модулю которого вычисляется символ.
    :return: Значение символа Лежандра: -1, 0 или 1.
    """
    # Если number делится на prime, символ Лежандра равен 0
    if number % prime == 0:
        return 0

    # Критерий Эйлера: вычисляем number^((prime - 1) / 2) mod prime
    euler_criterion = pow(number, (prime - 1) // 2, prime)

    # Если результат равен prime - 1, это эквивалентно -1 по модулю prime
    if euler_criterion == prime - 1:
        return -1
    return euler_criterion

