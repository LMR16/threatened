import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

path = Path("archive/especies.csv")
engine = create_engine('postgresql://postgres:postgres@localhost:5432/threatened')

def main():

    csv = read_csv(path)

    df = pd.DataFrame(csv)

    filtered_data = df[(df["Grupão"] == "Fauna") & (df["Grupo"] == "Aves")]
    
    filtered_data.to_sql('threatended_fil', engine, if_exists="replace")


def read_csv(path):
    csv = pd.read_csv(path, sep=';', encoding='latin-1')
    return csv