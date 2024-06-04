import pandas as pd
from pathlib import Path


path = Path("archive/especies.csv")

def read_csv(path):
    csv = pd.read_csv(path, sep=';', encoding='latin-1')
    return csv

csv = read_csv(path)

print(csv)