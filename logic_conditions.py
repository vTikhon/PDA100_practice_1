# Задание
# Записать логическое выражение определяющее, что число А является трехзначным

# number = 545
# print(len(str(number)) == 3)



# Задание
# Записать условие, которое является истинным, когда целое А не кратно трем и оканчивается нулем.

# a = 230
# print(a % 3 != 0 and a % 10 == 0)



# Задание
# Записать логическое выражение, которые определяет, что число А является четырехзначным, но не равно 4999.

# a = 4999.1
# print(1000 <= a <= 9999 and a != 4999)
# print(len(str(a)) == 4 and a != 4999)
# print(a in range(1000, 10000) and a != 4999)




# Задание
# Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.

# number_1 = float(input('Введите первое число: '))
# number_2 = float(input('Введите второе число: '))
# number_3 = float(input('Введите третье число: '))
# check = (number_1 < 45) + (number_2 < 45) + (number_3 < 45) == 1
# print(check)




# Задание
# Записать условие, которое является истинным, когда только одно из чисел А и В четное.

# number_1 = float(input('Введите первое число: '))
# number_2 = float(input('Введите второе число: '))
# check = (number_1 % 2 == 0) + (number_2 % 2 == 0) == 1
# print(check)