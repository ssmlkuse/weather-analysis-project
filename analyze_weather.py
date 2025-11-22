import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
plt.plot(df['date'], df['temperature'])
plt.title('Температура в Калужской области')
plt.xlabel('Дата')
plt.ylabel('Температура (°C)')
plt.grid()
plt.show()