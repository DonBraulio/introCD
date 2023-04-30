# %%
from pathlib import Path

import pandas as pd

# %%
data_dir = Path("data") / "viajes_stm"
df_viajes = pd.read_csv(data_dir / "viajes_stm_022023.csv")

# %%
df_viajes

# %%
df_viajes["con_tarjeta"].value_counts()

# %%
# Tramos por viaje: contamos cuantos viajes hay con cada número de tramos
count = df_viajes[["con_tarjeta", "id_viaje"]].groupby("id_viaje").count()
count.value_counts()
# Hay un viaje con 20 tramos!

# %%
# Cantidad de pasajeros
df_viajes["cantidad_pasajeros"].value_counts()
# No entiendo bien este campo. Puede haber viajes con muchos pasajeros? Hay hasta 29!
# %%
# Cuenta por empresa
df_viajes["descrip_empresa"].value_counts()

# %%
# Cuenta por Línea de ómnibus. 103 es el más popular
df_viajes["dsc_linea"].value_counts()

# %%
# Cuenta por paradas de origen
df_viajes["codigo_parada_origen"].value_counts()
# Hay información geográfica en formato GIS:
# https://geoweb.montevideo.gub.uy/geonetwork/srv/spa/catalog.search#/metadata/c6ea0476-9804-424a-9fae-2ac8ce2eee31

# %%
