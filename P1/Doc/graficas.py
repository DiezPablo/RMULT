import matplotlib.pyplot as plot
import pandas as pd

emulador2 = pd.read_csv('Emulador3_Tiempos')

lista_tiempos_em2 = emulador2['Time']
print(lista_tiempos_em2)

plot.hist(lista_tiempos_em2, density = 10, bins = 20)
plot.show()