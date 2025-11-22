import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('wind_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['wind_speed_kmh'], marker='o')
plt.title('Скорость ветра в Калужской области')
plt.xlabel('Дата')
plt.ylabel('Скорость ветра (км/ч)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()