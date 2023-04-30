# %%
from time import time
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

# %%
data_dir = Path("data") / "shakespeare"
data_dir.mkdir(parents=True, exist_ok=True)


def load_table(table_name, engine):
    """
    Leer la tabla con SQL y guardarla como CSV,
    o cargarla desde el CSV si ya existe
    """
    path_table = data_dir / f"{table_name}.csv"
    if not path_table.exists():
        print(f"Consultando tabla con SQL: {table_name}")
        t0 = time()
        df_table = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        t1 = time()
        print(f"Tiempo: {t1 - t0:.1f} segundos")

        print(f"Guardando: {path_table}\n")
        df_table.to_csv(path_table)
    else:
        print(f"Cargando tabla desde CSV: {path_table}")
        df_table = pd.read_csv(path_table, index_col=[0])
    return df_table


print("Conectando a la base...")
conn_str = "mysql+pymysql://guest:relational@relational.fit.cvut.cz:3306/Shakespeare"
engine = create_engine(conn_str)

# Todas las obras:
works = load_table("works", engine)

# Todos los párrafos de cada obra, por personaje:
paragraphs = load_table("paragraphs", engine)

# Tabla con cada capítulo de cada obra:
chapters = load_table("chapters", engine)

# Personajes posibles para cada párrafo de todas las obras
characters = load_table("characters", engine)

# %%
# Veamos las obras incluídas:
works

# %%
# Capítulos
chapters

# %%
# Personajes
characters

# %%
# Todos los párrafos
paragraphs

# %%
# Veamos el texto completo de algunos párrafos
print(paragraphs.iloc[0]["PlainText"])

# %%
print(paragraphs.iloc[1]["PlainText"])
# %%
