import pandas as pd
from datetime import datetime

data = [
    ['01/01/2023 00:00', 'A1', 'USER2'],
    ['01/01/2023 00:00', 'A1', 'USER3'],
    ['06/01/2023 00:00', 'A1', 'USER1'],
    ['05/12/2022 00:00', 'A1', 'USER1'],
    ['24/12/2022 00:00', 'A1', 'USER2'],
    ['08/12/2022 00:00', 'A1', 'USER3'],
    ['10/12/2022 00:00', 'A1', 'USER4'],
    ['13/01/2023 00:00', 'A1', 'USER4'],
    ['15/01/2023 00:00', 'A2', 'USER4'],
    ['17/12/2022 00:00', 'A2', 'USER4'],
    ['25/12/2022 00:00', 'A3', 'USER6'],
    ['25/12/2022 00:00', 'A3', 'USER6'],
    ['05/12/2022 00:00', 'A3', 'USER6'],
    ['07/01/2023 00:00', 'A1', 'USER7'],
    ['02/01/2023 00:00', 'A1', 'USER8'],
    ['06/01/2023 00:00', 'A2', 'USER5'],
    ['05/12/2022 00:00', 'A1', 'USER8']
]

df = pd.DataFrame(data, columns=['Date', 'account_id', 'user_id'])

df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y %H:%M')

df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

dez_2022 = df[(df['Month'] == 12) & (df['Year'] == 2022)]
jan_2023 = df[(df['Month'] == 1) & (df['Year'] == 2023)]

dez_users = dez_2022.groupby('account_id')['user_id'].unique().reset_index()
dez_users.rename(columns={'user_id': 'dez_users'}, inplace=True)

jan_users = jan_2023.groupby('account_id')['user_id'].unique().reset_index()
jan_users.rename(columns={'user_id': 'jan_users'}, inplace=True)

retention_df = pd.merge(dez_users, jan_users, on='account_id', how='outer')

def calculate_retention(row):
    dez = set(row['dez_users']) if isinstance(row['dez_users'], list) else set()
    jan = set(row['jan_users']) if isinstance(row['jan_users'], list) else set()
    
    if len(dez) == 0:
        return 0  
    
    retained = dez.intersection(jan)
    return len(retained) / len(dez) * 100

retention_df['retention_rate'] = retention_df.apply(calculate_retention, axis=1)

result = retention_df.sort_values('retention_rate', ascending=False)

print("Taxas de Retenção (Dez/2022 para Jan/2023):")
print(result[['account_id', 'retention_rate']].to_string(index=False))

max_retention = result.iloc[0]
print(f"\nO account_id com maior taxa de retenção é {max_retention['account_id']} com {max_retention['retention_rate']:.2f}%")
