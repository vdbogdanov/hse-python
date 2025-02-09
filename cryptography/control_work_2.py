from modules.Cryptography import Cryptography

# Контрольная работа 2. Вариант №3.

# # Задание 1
# # Вычислить 1137^(−1) (mod 2577)
task1 = Cryptography()
print(task1.euclid_extended(a=2577, b=1137))

# # Задание 2
# # Решить систему уравнений: x ≡ b (mod m)
# # x ≡ 7 (mod 15)
# # x ≡ 19 (mod 22)
# # x ≡ 16 (mod 19)
task2 = Cryptography()
equations = [
    {"b": 7, "m": 15},
    {"b": 19, "m": 22},
    {"b": 16, "m": 19}
]
print(task2.comparison_systems(equations))

# Задание 3
# Решить сравнение 196𝑥 ≡ 329 (mod 1253)
task3 = Cryptography()
print(task3.comparison_one(a=196, b=329, m=1253))

# Задание 4
# Решить сравнение x^2 ≡ 420 (mod 1049)
# print(Cryptography().legendre_symbol(a=561, p=757))