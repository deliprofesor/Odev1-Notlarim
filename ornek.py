print('Merhaba Girvak! Bu benim ilk ödevim.')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Basit bir veri kümesi oluşturuluyor
data = {
    'Yaş': [23, 45, 22, 36, 30, 40, 50, 29, 33, 24],
    'Gelir': [50000, 100000, 45000, 60000, 70000, 80000, 120000, 55000, 95000, 54000],
    'Eğitim Seviyesi': ['Lise', 'Üniversite', 'Lise', 'Üniversite', 'Üniversite', 'Üniversite', 'Lise', 'Üniversite', 'Lise', 'Lise']
}

# Veri çerçevesi oluşturuluyor
df = pd.DataFrame(data)

# İlk 5 satırı görüntüleyelim
print("Veri Kümesi İlk 5 Satır:")
print(df.head())

# Temel istatistiksel bilgiler
print("\nTemel İstatistiksel Özet:")
print(df.describe())

# Eğitim seviyesine göre gelir ortalamalarını hesaplayalım
print("\nEğitim Seviyelerine Göre Gelir Ortalamaları:")
print(df.groupby('Eğitim Seviyesi')['Gelir'].mean())

# Yaş ve gelir arasındaki ilişkiyi görselleştirelim
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Yaş', y='Gelir', data=df)
plt.title('Yaş ve Gelir İlişkisi')
plt.xlabel('Yaş')
plt.ylabel('Gelir')
plt.show()

# Gelir dağılımını görselleştirelim
plt.figure(figsize=(8, 5))
sns.histplot(df['Gelir'], kde=True, color='blue')
plt.title('Gelir Dağılımı')
plt.xlabel('Gelir')
plt.ylabel('Frekans')
plt.show()

# Yaşın ve gelirle olan korelasyonunu hesaplayalım
print("\nYaş ve Gelir Arasındaki Korelasyon:")
print(df[['Yaş', 'Gelir']].corr())


