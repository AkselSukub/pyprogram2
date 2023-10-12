print("<Количество цифр в числе>")
chisl = int(input("Введите число: "))
count = 0
while chisl > 0:
    count = count + 1
    chisl = chisl // 10
print("Количество цифр равно:", count)