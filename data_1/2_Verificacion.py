import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json

# Definir los vectores v1, v2, v3
# Definir los vectores v1, v2, v3, v4
v1 = np.array([32,73,68,72,69,72,72,70,72,71,74,77,76,82,82,92,106,103,104,103,31,69,70,72,71,73,76,74,70,75,76,79,80,81,85,97,106,106,104,103,31,71,72,72,74,74,74,75,77,76,79,79,82,85,86,101,108,109,106,105,39,71,71,72,75,76,79,76,79,78,80,79,81,84,90,104,108,110,110,108,35,72,72,75,76,77,79,81,78,79,79,80,32,78,87,107,110,113,115,110,71,75,72,75,78,79,77,80,80,82,81,29,32,51,88,107,114,116,114,114,72,72,73,78,78,80,81,80,80,75,26,30,39,90,94,110,114,114,114,115,77,73,74,79,79,81,82,83,69,29,81,31,31,90,93,111,114,115,114,116,73,76,77,80,79,84,82,53,30,82,85,28,34,90,94,101,113,115,114,114,80,79,78,80,85,83,35,29,79,87,90,28,38,92,95,97,111,114,114,114,80,78,78,83,84,85,86,33,86,86,33,30,90,93,93,99,109,111,114,112,79,81,80,85,87,86,89,88,89,86,29,30,91,93,93,100,107,110,109,113,82,84,81,85,86,90,86,88,94,94,28,32,95,94,95,100,107,108,107,109,84,84,84,86,89,88,90,91,93,89,29,92,95,97,95,102,106,107,107,105,84,86,85,89,89,92,92,93,92,31,27,92,96,100,96,103,107,107,106,108,88,89,85,89,89,26,27,28,28,24,24,30,38,40,96,102,107,112,108,108,88,93,89,89,46,29,34,37,43,31,28,27,28,27,30,109,108,110,108,108,88,93,88,93,94,31,28,47,78,70,39,33,30,30,33,34,110,110,107,109,92,96,91,95,96,97,100,100,104,103,104,105,103,104,109,111,112,113,112,113,93,96,90,96,99,101,100,103,105,104,107,108,107,106,110,114,115,115,115,116], dtype=np.float32) / 255.0
v2 = np.array([67,68,69,72,72,73,72,74,72,76,74,75,77,78,77,79,79,87,100,103,67,69,71,70,74,73,74,75,76,75,75,77,78,80,81,82,81,90,103,103,70,73,76,76,74,76,75,69,61,79,79,77,79,80,80,83,86,94,103,107,72,72,75,77,76,76,35,30,33,32,78,81,83,83,82,84,85,100,106,106,76,77,79,77,76,31,28,80,79,31,79,80,85,86,86,86,85,102,107,106,76,76,77,79,80,27,81,83,82,74,58,85,88,88,89,89,87,104,108,107,79,80,79,79,76,28,84,83,86,81,39,87,87,89,91,89,93,107,108,108,80,82,85,84,35,28,87,86,86,62,82,90,92,93,92,92,94,108,111,109,83,83,88,87,86,88,90,93,92,30,92,94,93,93,94,96,96,110,111,109,85,86,86,87,86,92,91,93,93,30,93,93,96,94,96,96,98,114,111,114,82,87,89,90,93,93,94,93,38,34,96,97,98,99,96,99,101,112,116,114,87,87,88,93,96,94,95,59,31,105,100,101,100,101,100,100,102,112,117,117,86,88,90,92,29,26,29,30,100,101,100,101,105,103,103,104,105,114,117,118,89,91,94,43,25,25,25,31,102,102,103,103,105,106,105,106,107,119,121,117,92,91,96,35,28,28,28,33,38,104,106,105,106,107,107,107,107,119,122,120,92,93,96,98,28,30,31,32,30,34,35,107,109,108,110,108,113,121,121,123,94,98,98,99,100,101,99,37,35,30,32,34,96,112,111,110,113,125,122,121,94,97,99,101,103,104,106,107,107,107,40,106,110,110,111,113,115,125,124,121,94,100,101,102,104,105,108,107,111,111,111,113,114,115,114,114,119,129,126,124,96,98,101,103,106,108,108,112,112,110,113,113,115,115,115,117,119,128,127,127], dtype=np.float32) / 255.0
v3 = np.array([113,110,112,115,116,118,119,122,125,120,121,123,120,121,121,118,116,111,109,108,111,114,114,116,119,121,124,121,123,123,123,120,124,123,123,121,116,114,114,109,109,114,114,118,121,123,121,122,121,125,125,124,126,123,123,121,120,119,114,111,112,115,118,119,120,124,123,122,123,123,127,126,128,128,125,126,123,120,116,115,113,114,117,121,123,123,122,121,45,43,122,128,128,129,128,127,124,123,121,115,114,120,121,123,122,125,123,51,41,47,46,44,44,129,129,129,128,125,123,118,120,119,123,125,126,131,128,131,131,129,129,48,49,133,134,134,131,128,127,122,120,121,124,126,128,133,132,132,131,130,45,61,135,136,138,135,135,135,129,128,117,121,126,130,133,129,132,134,43,43,131,136,136,138,139,137,137,136,136,132,115,121,127,132,131,129,133,50,37,37,46,138,140,142,141,142,140,140,138,136,114,122,127,131,132,132,134,133,135,136,44,37,138,139,140,140,142,142,141,140,116,122,126,130,133,134,135,136,135,135,138,143,39,118,141,142,142,142,140,141,114,120,127,130,133,134,135,136,135,139,139,140,40,41,43,141,142,143,142,140,118,122,127,130,129,134,44,134,136,137,137,118,34,35,34,45,142,141,139,139,114,123,126,130,131,133,135,35,34,34,33,39,30,32,35,46,140,139,138,135,116,120,125,128,130,133,135,134,134,42,31,30,31,35,56,139,137,138,137,134,111,119,122,128,128,131,133,135,136,139,133,134,135,132,138,136,135,135,133,128,109,114,122,127,127,130,131,133,135,137,137,136,138,136,135,136,135,132,130,125,31,113,118,121,128,127,128,132,133,135,136,135,135,135,134,133,131,128,126,122,24,25,29,37,121,125,128,129,131,131,132,130,129,130,130,129,127,124,120,119], dtype=np.float32) / 255.0


# Cargar el modelo desde el archivo JSON
json_file = open('modelo__DATA.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# Cargar los pesos al modelo desde el archivo HDF5
model.load_weights('modelo_pesos__DATA.weights.h5')

# Hacer predicciones sobre v1, v2, v3, v4
prediccion_v1 = model.predict(np.expand_dims(v1, axis=0))
prediccion_v2 = model.predict(np.expand_dims(v2, axis=0))
prediccion_v3 = model.predict(np.expand_dims(v3, axis=0))

# Imprimir resultados de la predicción
print("Resultados de la predicción:")
print(f"Vector v1, Tipo 1, Predicción: {np.argmax(prediccion_v1)}")
print(f"Vector v2, Tipo 2, Predicción: {np.argmax(prediccion_v2)}")
print(f"Vector v3, Tipo 3, Predicción: {np.argmax(prediccion_v3)}")