import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

df = pd.read_csv("../Resultados/em3_port5005")

tiempos = df.Time

plt.xlabel("Retardo en milisengundos")
plt.ylabel("Numero de aparaciones")
plt.title("Retardo Emulador 3 - Receptor")
plt.hist(tiempos, bins= 'auto')
plt.show()