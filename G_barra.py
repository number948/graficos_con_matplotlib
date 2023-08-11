#Utiliza el módulo matplotlib para crear gráficos de barras, líneas o pastel a partir de datos que tengas. Puedes generar datos ficticios o utilizar datos reales si tienes acceso a ellos.

import matplotlib.pyplot as plt


categorias = ['A', 'B', 'C', 'D', 'E']
valores = [15, 24, 12, 8, 20]

plt.bar(categorias, valores)  # Crea el gráfico de barras

plt.bar(categorias, valores, color='pink', edgecolor='purple')  # Personaliza colores
plt.xlabel('Categorías')  # Etiqueta del eje X
plt.ylabel('Valores')      # Etiqueta del eje Y
plt.title('Gráfico de Barras')  # Título del gráfico

plt.show()
