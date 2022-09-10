import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('C:\\Users\\karol\\Documents\\VC_delay\\delays.csv',header=None,delimiter=';')


p=df[0]
d=df[1]
print(df)
fig, ax = plt.subplots(figsize=(10,7))
ax.set_ylabel('Czas [s]')
ax.set_xlabel('Próbki')
ax.set_title('Opóźnienie trasmisji danych przez serwer FANUC Robot')
ax.bar(p,d,width=1, edgecolor="white", linewidth=0.1)
plt.show()