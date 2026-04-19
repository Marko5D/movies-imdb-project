import os
import pandas as pd

# Putanja do ulaznog CSV fajla
INPUT_FILE = "DMSP4-Task_02-movies.csv"

# Folder u koji ce biti sacuvani izlazni Excel fajlovi
OUTPUT_FOLDER = "output"

# Drzave koje se traze u zadatku
COUNTRIES = ["USA", "Russia", "UK", "South Korea"]

def load_data(file_path):
    """
    Ucitava CSV Fajl u DataFrame.
    """
    return pd.read_csv(file_path)

def prepare_numeric_columns(df):
    """
    Pretvara kolone budget i box_office u numericki tip podataka
    Ako postoje neispravne vrednosti, bice pretvorene u NaN.
    """
    df["budget"] = pd.to_numeric(df["budget"], errors="coerce")
    df["box_office"] = pd.to_numeric(df["box_office"], errors="coerce")
    return df

def process_country(df, country):
    """
    Za prosledjenu drzavu:
    1. Filtrira filmove,
    2. Kreira kolonu balance,
    3. Sortira po balance opadajuce,
    4. Uzima top 10 filmova,
    5. Ostavlja samo potrebne kolone.
    """
    # Filtriranje filmova za odredjenu drzavu
    country_df = df[df["country"].str.contains(country, na=False)].copy()

    # Kreiranje nove kolone balance
    country_df["balance"] = country_df["box_office"] - country_df["budget"]

    # Sortiranje po koloni balance od najvece ka najmanjoj vrednosti