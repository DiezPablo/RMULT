import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

df = pd.read_csv("../Doc/Emulador3_TiemposPuerto5005")

tiempos = df['Time']

labels, values = zip(*Counter(tiempos).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes,values,width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()