salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен



money_1 = spend
money_2 = spend + spend * 0.03
money_3 = money_2 + money_2 * 0.03
money_4 = money_3 + money_3 * 0.03
money_5 = money_4 + money_4 * 0.03
money_6 = money_5 + money_5 * 0.03
money_7 = money_6 + money_6 * 0.03
money_8 = money_7 + money_7 * 0.03
money_9 = money_8 + money_8 * 0.03
money_10 = money_9 + money_9 * 0.03

money_ = money_1 + money_2 + money_3 + money_4 + money_5 + money_6 + money_7 + money_8 + money_9 + money_10
need = money_ - salary * 10



need_money = need  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

print(round(need_money))
