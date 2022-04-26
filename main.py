tickets = int(input("Укажите количество билетов:"))
print("Укажите возраст посетителя:")
if tickets > 3:
    discount = 0.9
else:
    discount = 1
price = 0
for i in range(tickets):
    age = int(input("Возраст:"))
    if age < 18:
        price = price + 0
    elif 18 <= age < 25:
        price = price + 990
    else:
        price = price + 1390
print("Итого:", (price * discount))
