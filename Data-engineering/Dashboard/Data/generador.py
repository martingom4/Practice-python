import pandas as pd
import numpy as np

# definir los tipos de buques y rutas

def generar_data(tipos, rutas):
    # Generar datos simulados
    np.random.seed(42)  # Para reproducibilidad
    data= []
    for i in range(100):  # Generar 100 registros
        buque = np.random.choice(tipos)
        ruta = np.random.choice(rutas)
        distancia = ruta['distancia']
        # Valores base hipotéticos de consumo y emisiones por tipo de buque
        if buque == 'Portacontenedores':
            consumo_base = 200  # toneladas por 1000 millas náuticas
            emisiones_base = 600  # toneladas de CO₂ por 1000 millas náuticas
        elif buque == 'Petrolero':
            consumo_base = 250
            emisiones_base = 750
        elif buque == 'Granelero':
            consumo_base = 220
            emisiones_base = 660
        else:  # Pasajeros
            consumo_base = 300
            emisiones_base = 900
        # Calcular consumo y emisiones con variabilidad
        consumo = (consumo_base / 1000) * distancia * np.random.uniform(0.9, 1.1)
        emisiones = (emisiones_base / 1000) * distancia * np.random.uniform(0.9, 1.1)
        tiempo_viaje = distancia / np.random.uniform(20, 25)  # Velocidad entre 20-25 nudos
        eficiencia = emisiones / distancia  # Emisiones por milla náutica
        data.append({
            'ID_Buque': f'B{i+1:03d}',
            'Tipo_Buque': buque,
            'Origen': ruta['origen'],
            'Destino': ruta['destino'],
            'Distancia_mn': distancia,
            'Consumo_toneladas': consumo,
            'Emisiones_CO2_toneladas': emisiones,
            'Tiempo_Viaje_horas': tiempo_viaje,
            'Eficiencia_tonCO2_mn': eficiencia
        })
    return data

def guardar(data):
    return data.to_csv('data.csv', index=False, sep = ';')



tipos_buques = ['Portacontenedores', 'Petrolero','Granelero','Pasajeros']
rutas = [
        {'origen': 'Puerto A', 'destino': 'Puerto B', 'distancia': 1500},
        {'origen': 'Puerto C', 'destino': 'Puerto D', 'distancia': 3000},
        # Agregar más rutas según sea necesario
    ]
# Crear DataFrame
df = pd.DataFrame(generar_data(tipos_buques, rutas))
guardar(df)

print(df.head())
