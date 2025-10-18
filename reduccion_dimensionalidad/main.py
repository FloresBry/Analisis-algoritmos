import base64
from sklearn.cluster import KMeans
from io import BytesIO
from timeit import default_timer as timer
import numpy as np
import pandas as pd  
import tmap as tm
from faerun import Faerun
from PIL import Image
import matplotlib.pyplot as plt
#aqui eliges el cluster
ETIQUETA_ESPECIFICA_NUM=7
NOMBRE_ETIQUETA='ZAPATOS'
#configuracion necesaria
CFG = tm.LayoutConfiguration()
CFG.node_size = 1 / 55
#se cargan los datos y se dividen segun el cluster que hayas escogido
TEST_CSV_FILE = "fashion-mnist_test.csv" 
print(f"Cargando datos desde: {TEST_CSV_FILE}")
df_test = pd.read_csv(TEST_CSV_FILE)
df_filtrado=df_test[df_test['label']==ETIQUETA_ESPECIFICA_NUM]
LABELS_TEST = df_test['label'].values.astype(np.uint8) 
IMAGES_TEST = df_test.iloc[:, 1:].values.astype(np.uint8)
LABELS_FILTRADAS = df_filtrado['label'].values.astype(np.uint8)
IMAGENES_FILTRADAS = df_filtrado.iloc[:, 1:].values.astype(np.uint8) 
IMAGENES_FILTRO = IMAGENES_FILTRADAS
ETIQUETAS_FILTRO = LABELS_FILTRADAS 
ALL_IMAGES = IMAGES_TEST
ALL_LABELS = LABELS_TEST


#leyendas para el mapa
legend_labels = [
        (0, "Camisa o top"),
        (1, "Trouser"),
        (2, "Pullover"),
        (3, "Dress"),
        (4, "Coat"),
        (5, "Sandal"),
        (6, "Shirt"),
        (7, "Sneaker"),
        (8, "Bag"),
        (9, "Ankle boot"),
    ]


faerun = Faerun(clear_color="#111111", view="front", coords=False)

def main(LABELS_IMG, IMAGES, legend,nombre_archivo):

    imagen_label=[]
    dims = 1024
    enc = tm.Minhash(28 * 28, 42, dims)
    lf = tm.LSHForest(dims * 2, 128)
    
    print("Converting images ...")
    
    for image in IMAGES:
        
        img = Image.fromarray(np.uint8(np.split(np.array(image), 28)))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        imagen_label.append(
            "data:image/bmp;base64," + str(img_str).replace("b'", "").replace("'", "")
        )
        
    tmp = []

    for _, image in enumerate(IMAGES):
        tmp.append(tm.VectorFloat(image / 255))

    print("Running tmap ...")
    start = timer()
    lf.batch_add(enc.batch_from_weight_array(tmp))
    lf.index()
    x, y, s, t, _ = tm.layout_from_lsh_forest(lf, CFG)
    print("tmap: " + str(timer() - start))

    faerun.add_scatter(
        "FMNIST",
        {"x": x, "y": y, "c": LABELS_IMG, "labels": imagen_label},
        colormap="tab10",
        shader="smoothCircle",
        point_scale=4,
        max_point_size=10,
        has_legend=True,
        categorical=True,
        legend_labels=legend,
    )
    faerun.add_tree(
        "FMNIST_tree", {"from": s, "to": t}, point_helper="FMNIST", color="#FFFEFE"
    )
    faerun.plot(nombre_archivo, template="url_image")


if __name__ == "__main__":
    #tmap total, osea todos los datos
    nombre_archivo="fmnist_total"
    main(ALL_LABELS,ALL_IMAGES,legend_labels,nombre_archivo)
    #tmap solo del cluster
    nombre_archivo="fmnist_cluster"
    main(ETIQUETAS_FILTRO,IMAGENES_FILTRO,[(1,"Zapatos")],nombre_archivo)
    #recolectamos las imagenes del cluster y las ponemos en matplotlib
    imagenes_cluster=[]
    i=0
    for image in IMAGENES_FILTRO: 
        imagenes_cluster.append(Image.fromarray(np.uint8(np.split(np.array(image), 28))))
        buffered = BytesIO()
        imagenes_cluster[i].save(buffered, format="JPEG")
        i+=1
    num_imagenes=len(imagenes_cluster)
    columnas=40
    
    filas=int(np.ceil(num_imagenes/columnas))
    fig, axes=plt.subplots(filas,columnas,figsize=(10,10))
    
    axes=axes.flatten()
    for i,imagen_pil in enumerate(imagenes_cluster):
        imagen_np=np.array(imagen_pil)
        axes[i].imshow(imagen_np,cmap='gray')
        axes[i].axis('off')
    for j in range(num_imagenes,filas*columnas):
        fig.delaxes(axes[j])
    fig.suptitle(f"Cluster {NOMBRE_ETIQUETA}")
    plt.show()