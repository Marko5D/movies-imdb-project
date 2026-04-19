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
    country_df = country_df.sort_values(by="balance", ascending=False)

    # Uzimanje prvih 10 redova
    top_10 = country_df.head(10)

    # Zadrzavanje samo kolona koje su trazene u zadatku
    top_10 = top_10[["title," "release_year", "genre", "director", "balance"]]

    return top_10

def save_to_excel(df, country, output_folder):
    """
    Cuva DataFrame u Excel fajl unutar output foldera.
    """
    file_path = os.path.join(output_folder, f"top10_{country}.xlsx")
    df.to_excel(file_path, index=False)

def main():
    """
    Glavna funkcija programa.
    """

    # Kreiranje output foldera ako ne postoji
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Ucitavanje podataka
    df = load_data(INPUT_FILE)

    # Priprema numerickih kodova
    df = prepare_numeric_columns(df)

    # Obrada podataka za svaku drzavu i cuvanje u Excel fajl
    for country in COUNTRIES:
        result_df = process_country(df, country)
        save_to_excel(result_df, country, OUTPUT_FOLDER)
        print(f"Zavrsen excel fajl za drzavu: {country}")

    # Pokretanje programa
    if __name__ == "main":
        main()