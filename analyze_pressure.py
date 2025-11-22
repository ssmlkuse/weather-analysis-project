import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pressure_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')

plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['pressure_hpa'], color='blue', linewidth=2)
plt.title('Атмосферное давление в Калужской области')
plt.xlabel('Дата')
plt.ylabel('Давление (гПа)')
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()