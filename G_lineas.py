#Utiliza el módulo matplotlib para crear gráficos de barras, líneas o pastel a partir de datos que tengas. Puedes generar datos ficticios o utilizar datos reales si tienes acceso a ellos.

import matplotlib.pyplot as plt

#datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)  # Crea el gráfico de línea
plt.plot(x, y)
plt.xlabel('Eje X')         # Etiqueta para el eje X
plt.ylabel('Eje Y')         # Etiqueta para el eje Y
plt.title('Mi Primer Gráfico')  # Título del gráfico
plt.show()

