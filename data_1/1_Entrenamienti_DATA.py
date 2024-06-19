import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt


# Función para cargar datos desde un archivo txt y normalizar
def cargar_datos_desde_txt(file_path):
    vectors = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Leer datos de vectores
        for line in lines:
            if line.strip():  # asegurarse de que la línea no esté vacía
                vector = [int(num) for num in line.strip().split(',')]
                vectors.append(vector)

    # Convertir a numpy.ndarray y normalizar dividiendo por 255
    return np.array(vectors, dtype=np.float32) / 255.0

# Ruta al archivo de texto que contiene los datos
file_path = 'vectors_1.txt'

# Cargar datos desde el archivo y normalizar
data = cargar_datos_desde_txt(file_path)

# Verificar la cantidad de muestras en los datos
print(f"Número de muestras en data: {len(data)}")

# Generar etiquetas del 0 al 19 (para 20 vectores de entrada)
labels = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                   1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                   2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,])   # Esto crea un arreglo de numpy [0, 1, ..., 19]

# Crear el modelo de red neuronal
model = Sequential()
model.add(Dense(40, input_dim=400, activation='relu'))  # Capa Oculta 1, activación ReLU
model.add(Dense(30, activation='relu'))                # Capa Oculta 2, activación ReLU
model.add(Dense(10, activation='relu'))                # Capa Oculta 3, activación ReLU
model.add(Dense(20, activation='softmax'))             # Capa de Salida, activación Softmax para clasificación multiclase (20 clases)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Entrenar el modelo con las etiquetas y los datos normalizados
history = model.fit(data, labels, epochs=500, batch_size=1, verbose=1)


# Gráficos de precisión y pérdida
plt.figure(figsize=(8, 4))

# Gráfico de Precisión
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True)
# Gráfico de Pérdida
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.tight_layout()

# Definir los vectores v1, v2, v3, v4
v1 = np.array([29,66,67,67,68,68,70,67,69,69,72,74,78,77,78,102,101,100,102,100,29,67,67,66,66,71,68,68,70,69,74,75,76,79,83,102,102,105,105,101,35,68,68,68,71,72,71,75,73,73,75,75,81,79,83,105,107,106,105,104,67,70,69,70,73,72,75,72,75,75,79,79,40,80,86,107,107,107,109,106,69,72,72,73,74,73,72,71,76,76,76,39,56,80,84,106,107,109,111,108,70,70,71,72,77,76,75,78,75,79,30,27,36,82,86,109,109,109,111,109,71,71,70,73,73,78,75,78,79,30,31,30,33,84,90,109,110,112,112,111,74,69,72,75,75,78,77,75,28,33,77,29,33,86,89,110,109,112,109,115,75,74,72,76,79,80,77,27,30,83,43,29,79,86,92,103,111,110,110,111,72,75,75,74,77,79,35,27,79,82,30,29,86,88,90,105,107,111,110,109,73,75,76,79,80,80,79,80,83,84,28,29,86,89,90,100,105,109,108,111,77,75,77,81,82,85,84,82,86,84,28,33,88,90,91,100,106,106,107,107,76,77,78,82,85,84,83,85,87,89,25,88,88,88,90,101,103,104,103,105,79,79,79,86,85,87,85,86,86,29,28,86,90,90,94,103,104,105,101,104,82,80,80,81,86,86,86,89,87,27,28,89,90,92,94,102,105,102,103,103,84,83,83,86,29,23,24,26,28,27,26,28,31,33,37,103,104,104,106,102,85,85,84,85,28,27,30,32,36,37,31,27,26,28,28,99,103,104,105,100,85,87,84,87,90,30,90,95,90,93,88,36,30,29,36,37,103,107,106,106,86,91,86,88,92,94,95,95,99,98,97,99,99,99,104,107,107,107,108,108,91,91,88,90,93,94,97,97,98,97,100,101,100,100,107,108,109,111,108,109], dtype=np.float32) / 255.0
v2 = np.array([68,67,69,68,68,74,73,71,73,77,76,77,75,77,79,79,79,80,100,100,68,68,71,71,73,76,72,72,76,74,75,76,79,81,79,81,83,84,100,100,67,70,72,74,75,76,77,77,37,36,79,79,79,81,80,84,80,87,100,100,74,74,73,74,76,78,75,28,34,35,42,80,80,84,85,83,85,88,104,102,73,78,78,78,79,79,30,40,80,82,31,82,85,86,86,86,86,94,106,104,75,78,78,78,80,30,27,84,80,79,34,83,86,86,89,86,90,95,105,103,77,78,81,82,85,28,30,84,84,86,32,86,91,88,88,89,90,100,107,107,81,81,82,86,86,33,34,87,89,88,32,89,93,92,93,94,90,104,108,107,80,84,84,87,86,86,89,89,91,90,30,90,93,93,97,94,95,107,108,107,82,84,86,86,88,92,92,93,92,43,34,94,95,95,96,93,97,109,110,109,85,86,87,91,90,93,93,93,95,31,39,95,99,99,98,100,101,108,113,113,85,88,90,91,94,93,93,49,30,35,100,101,100,101,100,100,100,106,114,114,87,90,91,93,26,26,25,28,31,100,101,102,102,105,101,103,102,107,114,118,89,92,94,94,29,24,27,30,76,101,103,107,106,103,105,107,105,113,117,118,91,93,95,97,30,26,27,30,29,36,102,107,107,107,106,106,109,116,121,121,93,93,97,97,93,30,31,30,31,30,31,45,108,107,107,109,108,121,119,121,93,95,95,100,101,100,102,102,78,31,30,30,37,109,111,110,111,121,122,120,96,97,97,100,103,104,105,107,108,107,107,42,110,110,111,114,113,124,125,124,94,97,99,100,103,105,106,107,109,110,111,110,112,112,114,114,115,124,125,125,96,100,100,101,105,108,108,109,111,112,111,113,115,115,117,118,117,127,126,124], dtype=np.float32) / 255.0
v3 = np.array([112,113,117,114,115,118,119,121,121,120,122,119,121,119,118,114,115,114,109,110,110,113,115,114,117,121,121,118,122,122,124,121,121,123,119,120,115,113,113,111,111,114,115,116,121,121,121,123,124,124,124,123,127,122,123,122,120,117,115,110,114,114,116,118,121,123,123,122,124,122,127,126,128,126,126,123,123,121,117,114,111,117,118,119,123,122,123,124,45,51,121,125,127,128,127,127,127,122,119,116,115,121,121,122,124,124,123,49,41,46,45,45,43,130,131,129,126,127,123,119,119,121,125,125,125,131,128,131,130,130,127,44,47,132,134,134,130,129,126,122,116,123,125,128,129,132,131,132,132,131,43,73,133,137,136,135,135,133,133,127,115,122,127,130,131,131,133,133,37,40,132,137,136,140,139,137,137,137,135,134,118,122,127,132,133,132,132,40,35,37,41,137,138,142,140,141,139,142,138,138,114,121,128,131,132,132,135,135,135,135,44,41,137,138,141,138,141,142,142,140,116,121,128,129,132,135,135,135,136,139,140,144,39,113,142,142,142,143,143,142,116,121,125,130,133,134,135,135,137,138,140,140,37,40,40,142,142,142,140,141,118,121,125,130,132,134,46,136,138,137,135,89,34,34,33,64,142,141,140,135,114,122,125,131,131,133,133,37,36,35,34,43,33,32,34,47,140,138,137,136,115,120,124,127,130,135,135,136,130,40,35,32,30,36,84,137,137,136,135,133,113,119,122,128,128,131,134,135,136,137,138,135,138,135,140,137,136,134,134,129,106,115,123,127,127,127,130,132,136,135,136,135,137,135,135,135,134,134,128,126,28,108,117,123,126,128,130,132,134,135,134,135,135,135,133,133,131,128,125,121,22,25,27,37,120,127,126,129,130,132,132,131,129,130,130,128,128,126,121,118], dtype=np.float32) / 255.0


# Hacer predicciones sobre v1, v2, v3, v4
prediccion_v1 = model.predict(np.expand_dims(v1, axis=0))
prediccion_v2 = model.predict(np.expand_dims(v2, axis=0))
prediccion_v3 = model.predict(np.expand_dims(v3, axis=0))

# Imprimir resultados de la predicción
print("Resultados de la predicción:")
print(f"Vector v1, Predicción: {np.argmax(prediccion_v1)}")
print(f"Vector v2, Predicción: {np.argmax(prediccion_v2)}")
print(f"Vector v3, Predicción: {np.argmax(prediccion_v3)}")

plt.show()

# Guardar el modelo en dos partes separadas: JSON y pesos en HDF5
# Serializar el modelo a JSON
model_json = model.to_json()
with open("modelo__DATA.json", "w") as json_file:
    json_file.write(model_json)

# Serializar los pesos a HDF5
model.save_weights("modelo_pesos__DATA.weights.h5")
print("Modelo Guardado!")