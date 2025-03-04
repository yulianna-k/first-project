import math

# Открываем входной файл для чтения
with open("INPUT.TXT", "r") as input_file:
    # Читаем значения a и b
    a = int(input_file.readline().strip())
    b = int(input_file.readline().strip())

# Вычисляем гипотенузу по теореме Пифагора
c = math.sqrt(a**2 + b**2)

# Открываем выходной файл для записи
with open("../../Downloads/OUTPUT.TXT", "w") as output_file:
    # Записываем результат в файл, форматируем результат с одной цифрой после точки
    output_file.write(f"{c:.1f}\n")
