import requests
import os

IP = "http://<ip_alpine>:5000"

OUTPUT_DIR = "imagenes_resultado"
os.makedirs(OUTPUT_DIR, exist_ok=True)

dataset = "iris"
model = "RandomForest"

train_sizes = [round(i / 10, 1) for i in range(1, 10)]
test_sizes = [round(1 - t, 1) for t in train_sizes]

for tr, ts in zip(train_sizes, test_sizes):

    url = f"{IP}/train"

    data = {
        "dataset": dataset,
        "model": model,
        "train_size": tr,
        "test_size": ts
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("Error en la peticion con train_size =", tr, "test_size =", ts)
        continue

    image_name = f"{dataset}Tr{tr}Tst{ts}.png"
    image_url = f"{IP}/static/{image_name}"

    imagen = requests.get(image_url)

    if imagen.status_code == 200:
        ruta_guardado = os.path.join(OUTPUT_DIR, image_name)
        with open(ruta_guardado, "wb") as f:
            f.write(imagen.content)
        print("Imagen descargada:", ruta_guardado)
    else:
        print("No se encontro la imagen generada:", image_url)
