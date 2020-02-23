import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

df = pd.read_csv("../Resultados/em2_5005")

tiempos = df.Time

plt.hist(tiempos, bins= 'auto')
plt.show()
s