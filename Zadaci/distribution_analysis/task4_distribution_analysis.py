import pandas as pd

# Učitavanje podataka
df = pd.read_csv("online_store_data.csv")

# pretvaranje u numeričke vrednosti
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["num_of_ratings"] = pd.to_numeric(df["num_of_ratings"], errors="coerce")
df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce")

# 1. OPSEG OCENA ZA TELEVIZORE

def analyze_tv_ratings_range(df):
    """ Racuna razliku izmedju najbolje i najlosije ocenjenog TV-a """

    # filtriranje TV-a
    tvs = df[df["category"] == "TVs"]

    # uklanjanje NaN vrednosti
    tvs = tvs.dropna(subset=["rating"])

    # provera da li ima podataka
    if tvs.empty:
        print("\n1. Nema TV proizvoda sa validnim ocenama.")
        return

    min_rating = tvs["rating"].min()
    max_rating = tvs["rating"].max()

    rating_range = max_rating - min_rating

    print("\n1. Razlika izmedju najbolje i najlosije ocenjenog TV-a:")
    print("Min ocena:", min_rating)
    print("Max ocena:", max_rating)
    print("Opseg:", rating_range)


# 2. IQR ZA CENE SMARTPHONE-A

def analyze_smartphone_price_iqr(df):
    """ Racuna interkvartilni opseg cena za pametne telefone """

    # filtriranje samo smartphone proizvoda
    smartphones = df[df["category"] == "Smartphones"]

    # kvartili
    q1 = smartphones["price"].quantile(0.25)
    q3 = smartphones["price"].quantile(0.75)

    # IQR
    iqr = q3 - q1

    print("\n2. Cenovni rang (IQR) za pametne telefone:")
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print(df.columns)

# 3. NAJUJEDNAČENIJI BRENDOVI

def analyze_brand_consistency(df):
    """ Aproksimacija: proizvodi sa najstabilnijim (najvišim) ocenama """

    # izbacujemo NaN
    clean_df = df.dropna(subset=["rating"])

    # sortiranje po oceni (najmanja varijacija ≈ najstabilnije visoke ocene)
    top5 = clean_df.sort_values("rating", ascending=False).head(5)

    print("\n3. 5 proizvoda sa najvisim i najstabilnijim ocenama:")
    print(top5[["brand", "name", "rating"]])


# 4. KVARTILI RECENZIJA I PRODAJA

def analyze_reviews_vs_sales(df):
    """ Analizira odnos izmedju broja ocena i prodaje """

    # kvartili za broj ocena
    q1 = df["num_of_ratings"].quantile(0.25)
    q2 = df["num_of_ratings"].quantile(0.50)
    q3 = df["num_of_ratings"].quantile(0.75)

    # funkcija za dodelu kvartila
    def assign_quartile(x):
        if x <= q1:
            return "1st quartile"
        elif x <= q2:
            return "2nd quartile"
        elif x <= q3:
            return "3rd quartile"
        else:
            return "4th quartile"

    # nova kolona
    df["rating_quartile"] = df["num_of_ratings"].apply(assign_quartile)

    # grupisanje i suma prodaje
    result = df.groupby("rating_quartile")["quantity_sold"].sum()

    print("\n4. Prodaja po kvartilima broja ocena:")
    print(result)


# POZIV FUNKCIJA

if __name__ == "__main__":
    analyze_tv_ratings_range(df)
    analyze_smartphone_price_iqr(df)
    analyze_brand_consistency(df)
    analyze_reviews_vs_sales(df)