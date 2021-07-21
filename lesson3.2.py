deposit = 2130 # изнaчальная сумма депозита
year = 5 #колличество лет
prosent = 10 # процент годовых
bonus = 120 #бонус каждый год

deposit_1_year = deposit + (deposit / 10) + 120 # сумма за 1 год
deposit_2_year = deposit_1_year + (deposit_1_year / 10) + 120 # сумма за 2 год
deposit_3_year = deposit_2_year + (deposit_2_year / 10) + 120 # сумма за 3 год
deposit_4_year = deposit_3_year + (deposit_3_year_ / 10) + 120 # сумма за 4 год
deposit_5_year = deposit_4_year + (deposit_4_year / 10) + 120 # сумма за 5 год
print(deposit_5_year) # конечная сумма за 5 лет