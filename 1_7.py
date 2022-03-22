a = int(input("Введите результаты первого дня -> "))
b = int(input("Введите Вашу цель -> "))
ind = 1
result = a
print(f"{ind}-й день: {result}")
while int(result) < b:
    ind += 1
    a = a + 0.1 * a
    result = round(a, 2)
    print(f"{ind}-й день: {result}")
print(f"На {ind}-й день Вы достигните результата - не менее {b} км")
