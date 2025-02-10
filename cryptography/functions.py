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
        result.append(f"q = a / b = {a} / {b} = {a // b}")
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


def comparison_x1(a, b, m):
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
                f"(x0 + {counter} * (b / НОД(a, m))) mod m = ({x0} + {counter} * ({b} / НОД({a}, {m}))) mod {m} = {(x0 + counter * m_reduced) % m}"
            )
            solutions.append((x0 + counter * m_reduced) % m)

        # Формирование результата
        result.append("")
        result.append(f"Решение сравнения {a}x = {b} (mod {m})")
        result.append(f"Множество решений: {solutions} (mod {m})")
        result.append(
            f"Эти решения образуют один класс вычетов по модулю m / НОД(a, m) = {m} / {gcd} = {m_reduced}"
        )

        # Форматирование результата
        result = f"\n{'\n'.join(result)}"

        print(result)

        return result

    else:
        raise Exception("Что-то пошло не так...")


def comparison_system(equations):
    """
    Решение систем сравнений первой степени с одним неизвестным.
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
        equation["N_output"] = f"N / m = {N} / {equation['m']} = {N // equation['m']}"
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


def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра (a|p) с использованием критерия Эйлера

    Параметры:
        a (int): Число, для которого вычисляется символ
        p (int): Простой модуль

    Возвращает:
        1, если a — квадратичный вычет по модулю p
        -1, если a — квадратичный невычет
        0, если a = 0 (mod p)
    """
    # Инициализация списка для вывода результата
    result = list()

    # Случай a = 0 (mod p)
    if a % p == 0:
        result.append(f"a = 0 (mod {p})")
        print(result)
        return 

    # Критерий Эйлера: a^((p-1)/2) mod p
    ls = pow(a, (p - 1) // 2, p)
    result.append(f"a^((p-1)/2) mod p = {a}^(({p}-1)/2) mod {p} = {ls}")

    # Если результат равен p-1, преобразуем его в -1 для удобства
    if ls == p - 1:
        ls = -1
        result.append(f"Критерий Эйлера равен p - 1 = {p} - 1 = {p-1}, преобразуем его в -1")

    # Форматирование результата
    result = "\n".join(result)

    print(result)

    return ls


def tonelli_shanks(a, p):
    """
    Алгоритм Тонелли-Шенкса для извлечения квадратных корней x² ≡ a (mod p)

    Параметры:
        a (int): Число, из которого извлекается корень
        p (int): Простой модуль

    Возвращает:
        tuple: Два корня (r, p-r) или None, если решения нет
    """
    # Шаг 1: Проверка существования решений через символ Лежандра
    print("\nШаг 1: Проверка существования решений через символ Лежандра:\n")
    if legendre_symbol(a, p) != 1:
        return None  # Нет решений

    # Шаг 2: Поиск квадратичного невычета b (нужен для построения последовательности)
    print("\nШаг 2: Поиск квадратичного невычета с помощью символа Лежандра\n")
    b = 2
    while legendre_symbol(b, p) != -1:
        b += 1

    # Шаг 3: Разложение p-1 в форму 2^s * t (t — нечётное)
    print("\nШаг 3: Разложение p-1 в форму 2^s * t (t — нечётное)\n")
    s, t = 0, p - 1
    print(f"s = 0, t = p-1 = {p-1}")
    while t % 2 == 0:
        print(f"s = {s} + 1 = {s+1}, t = {t} // 2 = {t // 2}")
        s += 1  # Степень двойки
        t //= 2  # Нечётный множитель

    # Шаг 4: Вычисление обратного элемента a^{-1} mod p (для упрощения формул)
    # a_inv = pow(a, p - 2, p) # Используется малая теорема Ферма
    # Используется расширенный алгоритм Евклида
    print("\nШаг 4: Вычисление обратного элемента a^{-1} mod p с помощью расширенного алгоритма Евклида")
    _, _, _, _, _, _, a_inv, _, _, _ = euclid_extended(a, p)
    a_inv %= p
    print(f"\nОбратный элемент a^{-1} mod p: {a_inv}\n")

    # Шаг 5: Уточнение корня (итерации по s-1)
    print(f"Шаг 5: Вычисление корней\n")

    c = pow(b, t, p)
    print(f"c = b^t mod p = {b}^{t} mod {p} = {c}")

    r = pow(a, (t + 1) // 2, p)
    print(f"r = a^(t+1)//2 mod p = {a}^({t+1}//2) mod {p} = {r}")

    print("\nПоследовательность c^(2^(s-1-i)) mod p:")
    c_powers = list()
    for i in range(s):
        print(f"c^(2^(s-1-{i})) mod p = {c}^(2^{s-1-i}) mod {p} = {pow(c, 1 << (s - 1 - i), p)}")
        c_powers.append(pow(c, 1 << (s - 1 - i), p))
    
    print("\nВычисление d = (r^2 * a^(-1))^(2^(s-2-i)) mod p:")
    for i in range(s - 1):
        # Вычисление d = (r^ * a^{-1})^(2^(s-2-i)) mod p
        d = pow((r * r) % p * a_inv % p, 1 << (s - 2 - i), p)
        print(f"d = ({r}^2 * {a}^(-1))^(2^({s}-2-{i})) mod {p} = {d}")

        # Если d ≡ -1 (mod p), корректируем корень
        if d != 1:
            print(f"d != 1 --> r = ({r} * {c_powers[i + 1]}) mod {p} = {(r * c_powers[i + 1]) % p}")
            r = (r * c_powers[i + 1]) % p # Умножаем на c^(2^(s-1-i))

        # Обновляем c = c^2 mod p для следующей итерации
        print(f"Обновление c = c^2 mod p для следующей итерации: c = (c * c) mod p = ({c}^2) mod {p} = {(c * c) % p}")
        c = (c * c) % p

    return (r, p - r) # Возвращаем оба корня (r и -r mod p)

def comparison_x2(a, p):
    """
    Решает сравнение x^2 ≡ a mod p и возвращает корни или None
    
    Параметры:
        a (int): Число в правой части сравнения
        p (int): Простой модуль
    
    Возвращает:
        tuple: Корни (r, p-r) или None, если решений нет
    """
    # Приведение a в диапазон [0, p-1]
    a = a % p

    # Случай a = 0 (mod p): единственный корень 0
    if a == 0:
        return (0,)
    
    # Используем алгоритм Тонелли-Шенкса
    roots = tonelli_shanks(a, p)

    if roots:
        print(f"\nКорни сравнения x^2 ≡ {a} mod {p}: {roots[0]} и {roots[1]}")
    else:
        print("\nРешений нет")

    return roots