import pandas as pd


class Cryptography:
    def __init__(
        self,
        q=None,
        r=None,
        x=None,
        y=None,
        a=None,
        b=None,
        x2=None,
        x1=None,
        y2=None,
        y1=None,
    ):
        self.q = q
        self.r = r
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1

    def euclid_simple(self, a, b):
        """
        Простой алгоритм Евклида
        """
        # Создание временных переменных
        a_tmp = a
        b_tmp = b
        output_list = list()

        # Простая версия алгоритма Евклида
        while b != 0:
            output_list.append(f"{a} % {b} = {a % b}")
            a, b = b, a % b

        # Установка аттрибутов класса
        self.a = a

        # Красивый вывод результата
        output_list.append(f"\nНОД({a_tmp}, {b_tmp}) = {a}")

        return f"\nВычисления:\n{'\n'.join(output_list)}"

    def euclid_extended(self, a, b):
        """
        Расширенный алгоритм Евклида
        """
        # Создание временных переменных
        a_tmp = a
        b_tmp = b
        output_list = list()
        cf_list = list()

        # Инициализация начальных значений для коэффициентов
        x2, x1 = 1, 0
        y2, y1 = 0, 1
        x, y = "-", "-"
        q, r = "-", "-"
        iteration = 1

        output_list.append("Итерация: 0")
        output_list.append(
            f"q = {q}, r = {r}, x = {x}, y = {y}, a = {a}, b = {b}, x2 = {x2}, x1 = {x1}, y2 = {y2}, y1 = {y1}"
        )
        output_list.append("")

        # Расширенная версия алгоритма Евклида
        while b != 0:

            # Добавление номера итерации в список
            output_list.append(f"Итерация: {iteration}")
            iteration += 1

            # Добавление коэффициентов в список
            cf_list.append([q, r, x, y, a, b, x2, x1, y2, y1])

            # Вычисление частного
            output_list.append(f"q = a // b = {a} / {b} = {a // b}")
            q = a // b

            # Вычисление остатка
            output_list.append(f"r = a mod b = {a} mod {b} = {a % b}")
            r = a % b

            # Обновление переменных
            output_list.append(f"a = b = {b}, b = r = {r}")
            a, b = b, r

            # Вычисление нового коэффициента x
            output_list.append(f"x = x2 - q * x1 = {x2} - {q} * {x1} = {x2 - q * x1}")
            x = x2 - q * x1

            # Вычисление нового коэффициента y
            output_list.append(f"y = y2 - q * y1 = {y2} - {q} * {y1} = {y2 - q * y1}")
            y = y2 - q * y1

            # Обновление промежуточных коэффициентов
            output_list.append(
                f"x2 = x1 = {x1}, x1 = x = {x}, y2 = y1 = {y1}, y1 = y = {y}"
            )
            x2, x1 = x1, x
            y2, y1 = y1, y

            # Заглушка для разделения итераций
            output_list.append("")

            # Установка аттрибутов класса
            if b == 0:
                self.q = q
                self.r = r
                self.x = x
                self.y = y
                self.a = a
                self.b = b
                self.x2 = x2
                self.x1 = x1
                self.y2 = y2
                self.y1 = y1

        # Добавление финальных значений в список
        cf_list.append([q, r, x, y, a, b, x2, x1, y2, y1])

        # Создание датафрейма
        df = pd.DataFrame(
            cf_list, columns=["q", "r", "x", "y", "a", "b", "x2", "x1", "y2", "y1"]
        )

        # Формирование списка с результатами
        output_list.append(f"НОД({a_tmp}, {b_tmp}) = {a}")
        output_list.append(f"Коэффициенты: x = {x2}, y = {y2}")
        output_list.append(
            f"Целочисленная линейная комбинация: {x2} * {a_tmp} + {y2} * {b_tmp} = {x2 *a_tmp + y2 * b_tmp}"
        )

        return f"\nТаблица коэффициентов:\n{df}\n\n{'\n'.join(output_list)}"

    def comparison_one(self, a, b, m):
        """
        Решение сравнений первой степени с одним неизвестным
        """
        # Используем расширенный алгоритм Евклида для нахождения НОД(a, m)
        print(self.euclid_extended(a, m))
        gcd = self.a  # НОД(a, m)

        # Случай 1: НОД(a, m) = 1
        if gcd == 1:
            x0 = (self.x2 * b) % m
            return f"\nРешение сравнения {a}x = {b} (mod {m}): x ≡ {x0} (mod {m})"

        # Случай 2: НОД(a, m) = d > 1 и d не делит b
        elif b % gcd != 0:
            return "\nРешение не существует, так как b не делится на НОД(a, m)."

        # Случай 3: НОД(a, m) = d > 1 и d делит b
        elif b % gcd == 0:
            a_reduced = a // gcd
            b_reduced = b // gcd
            m_reduced = m // gcd

            # Находим частное решение для сокращенного сравнения
            x0 = (self.x2 * b_reduced) % m_reduced

            # Формируем все d решений
            output_list = list()
            solutions = list()
            for counter in range(gcd):
                output_list.append(
                    f"(x0 + {counter} * (b // НОД(a, m))) mod m = ({x0} + {counter} * ({b} // НОД({a}, {m}))) mod {m} = {(x0 + counter * m_reduced) % m}"
                )
                solutions.append((x0 + counter * m_reduced) % m)

            # Формирование списка с результатами
            output_list.append(f"\nРешение сравнения {a}x = {b} (mod {m})")
            output_list.append(f"Множество решений: {solutions} (mod {m})")
            output_list.append(
                f"Эти решения образуют один класс вычетов по модулю m // НОД(a, m) = {m} // {gcd} = {m_reduced}"
            )

            return f"\n{'\n'.join(output_list)}"

        else:
            raise Exception("Что-то пошло не так...")

    def comparison_systems(self, equations):
        """
        Решение СИСТЕМ сравнений первой степени с одним неизвестным
        """
        # Вычисления значения вспомогательной переменной
        N = 1
        for equation in equations:
            N *= equation["m"]

        # Вычисление искомого значения
        a = 0
        for equation in equations:
            equation["N"] = N // equation['m']
            print(self.euclid_extended(a=equation['N'], b=equation['m']))
            a += equation["b"] * self.x2 * equation['N']
            equation["N_output"] = f"N // m = {N} // {equation['m']} = {N // equation['m']}"
            equation["a_output"] = f"{equation['b']} * {self.x2} * {equation['N']} = {equation['b'] * self.x2 * equation['N']}"

        # Формирование списка с результатами
        output_list = list()
        output_list.append("\nВычисление значения вспомогательных переменных:")
        output_list.append(f"N = {N}")
        output_list += [
            f"N{counter + 1} = {equations[counter]['N_output']}"
            for counter in range(len(equations))
        ]
        output_list.append("\nВычисление искомого значения:")
        output_list += [
            f"a{counter + 1} = {equations[counter]['a_output']}"
            for counter in range(len(equations))
        ]
        output_list.append(f"a = {a}")

        # Проверка результата
        output_list.append("\nПроверка результата:")
        for equation in equations:
            equation_check = f"{a} (mod {equation['m']}) = {a % equation['m']}"
            if a % equation["m"] == equation["b"]:
                output_list.append(f"{equation_check} OK")
            elif a % equation["m"] != equation["b"]:
                output_list.append(f"{equation_check} ERROR")
            else:
                raise Exception("Что-то пошло не так...")

        return '\n'.join(output_list)

    def legendre_symbol(self, number, prime):
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

    def comparison_two(self):
        return
