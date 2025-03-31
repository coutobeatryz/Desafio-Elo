#Projeto 01

from datetime import datetime, timedelta
from collections import defaultdict

dados = [
    ("2020-12-06", "A1", "U1"),
    ("2021-01-15", "A1", "U2"),
    ("2021-01-06", "A1", "U3"),
    ("2021-01-02", "A1", "U1"),
    ("2020-12-24", "A1", "U2"),
    ("2020-12-08", "A1", "U1"),
    ("2020-12-09", "A1", "U1"),
    ("2021-01-10", "A2", "U4"),
    ("2021-01-11", "A2", "U4"),
    ("2021-01-12", "A2", "U4"),
    ("2021-01-15", "A2", "U5"),
    ("2020-12-17", "A2", "U4"),
    ("2020-12-25", "A3", "U6"),
    ("2020-12-25", "A3", "U6"),
    ("2020-12-25", "A3", "U6"),
    ("2021-01-01", "A3", "U7"),
    ("2020-12-06", "A3", "U6"),
    ("2021-01-14", "A3", "U6"),
    ("2021-02-07", "A1", "U1"),
    ("2021-02-10", "A1", "U2"),
    ("2021-02-01", "A2", "U4"),
    ("2021-02-01", "A2", "U5")
]

user_access = defaultdict(set)

for date, account, user in dados:
    user_access[user].add(datetime.strptime(date, "%Y-%m-%d"))

usuarios_ativos = []
for user, dates in user_access.items():
    sorted_dates = sorted(dates)
    
    for i in range(len(sorted_dates) - 2):
        if sorted_dates[i + 1] == sorted_dates[i] + timedelta(days=1) and \
           sorted_dates[i + 2] == sorted_dates[i] + timedelta(days=2):
            usuarios_ativos.append(user)
            break  

print("Usuários que ficaram ativos por 3 dias:", usuarios_ativos)
