# Что нужно сделать:
# Посчитать сумму каждой продажи (количество × цена) и вывести список всех продаж с итогом по каждой
# Найти и вывести самую дорогую единичную продажу (по итоговой сумме)
# Посчитать общую выручку магазина за неделю
# Вывести только те продажи, где итоговая сумма больше 10 000 ₽
# Посчитать, сколько раз продавался каждый товар (суммарное количество штук)
#
# Требования:
# Весь код разбить на функции — одна функция = одна задача
# Отчёт выводить читаемо, с заголовками
# Не использовать словари (dict) — только списки, индексы и срезы


shop = [["Ноутбук", 2, 75000],
["Мышь", 5, 1200],
["Монитор", 1, 32000],
["Клавиатура", 3, 3500],
["Ноутбук", 1, 75000],
["Мышь", 2, 1200]]

print(shop)


def price_every_purchases():
    for x in shop:
        print(f"{x[0]} - {x[1] * x[2]} ₽")


def most_expensive_purchases():
    best = shop[0]
    for x in shop:
        if x[1] * x[2] > best[1] * best[2]:
            best = x
    print(f"Самая дорогая продажа: {best[0]} — {best[1] * best[2]} ₽")



def input_for_week():
    total = 0
    for x in shop:
        total += x[1] * x[2]
    print(f"Выручка за неделю: {total} ₽")


def purchases_more_than_10k():
    for x in shop:
        if (x[1] * x[2]) > 10000:
            print(f"{x[0]} - {x[1] * x[2]} ₽")

def how_much_item_was_purched():
    result = []
    for x in shop:
        found = False
        for item in result:
            if item[0] == x[0]:
                item[1] += x[1]
                found = True
        if not found:
            result.append([x[0], x[1]])
    for i in result:
        print(f"{i[0]} - {i[1]} шт.")


price_every_purchases()
most_expensive_purchases()
input_for_week()
purchases_more_than_10k()
how_much_item_was_purched()
