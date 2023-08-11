#Utiliza el módulo matplotlib para crear gráficos de barras, líneas o pastel a partir de datos que tengas. Puedes generar datos ficticios o utilizar datos reales si tienes acceso a ellos.

import matplotlib.pyplot as plt


etiquetas = ['Manzanas', 'Plátanos', 'Naranjas', 'Peras']
tamaños = [30, 25, 20, 15]

plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=140, colors=['red', 'green', 'orange', 'blue'])
plt.axis('equal')  # Hace que el gráfico sea circular en lugar de elíptico
plt.title('Gráfico de Torta')

plt.show()

