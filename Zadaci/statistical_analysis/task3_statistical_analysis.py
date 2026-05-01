import pandas as pd

# Ucitavanje podataka
df = pd.read_csv("online_store_data.csv")

# Rating (može imati zarez, tekst itd.)
df["rating"] = df["rating"].astype(str)
df["rating"] = df["rating"].str.replace(",", ".", regex=False)
df["rating"] = df["rating"].str.extract(r"(\d+\.?\d*)")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# Quantity kolone
df["quantity_sold"] = df["quantity_sold"].astype(str).str.replace(",", ".", regex=False)
df["quantity_sold"] = pd.to_numeric(df["quantity_sold"], errors="coerce")

df["quantity_in_stock"] = df["quantity_in_stock"].astype(str).str.replace(",", ".", regex=False)
df["quantity_in_stock"] = pd.to_numeric(df["quantity_in_stock"], errors="coerce")

# Mere centralne tendencije

def analyze_product_ratings(df):
    """ Racuna osnovne mere centralne tendencije za ocene proizvoda. """
    
    average_rating = df["rating"].mean()
    median_rating = df["rating"].median()
    mode_rating = df["rating"].mode()

    print("\n1. Prosecna ocena proizvoda u online trgovini")
    print("Aritmeticka sredina:", average_rating)
    print("Medijana:", median_rating)
    print("Mod:", mode_rating)

def analyze_most_common_brand(df):
    """ Pronalazi najcesci brend u online trgovini. """
    
    most_common_brand = df["brand"].mode()[0]

    print("\n2. Najcesci brend u online trgovini")
    print(most_common_brand)

# 2. Grupisanje i agregacija

def analyze_top_selling_brand(df):
    """ Pronalazi najprodavaniji brend. """
    
    top_selling_brand = (
        df.groupby("brand")["quantity_sold"]
        .sum()
        .sort_values(ascending=False)
        .head(1)
    )

    print("\n3. Najprodavaniji brend u online trgovini")
    print(top_selling_brand)

def analyze_average_rating_by_category(df):
    """ Racuna prosecnu ocenu po kategorijama. """
    
    average_rating_by_category = (
        df.groupby("category")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n4. Prosecna osena proizvoda po kategorijama")
    print(average_rating_by_category)

def analyze_popularity_by_color(df):
    """ Analiza popularnosti proizvoda po bojama. """
    
    popularity_by_color = (
        df.groupby("color")["quantity_sold"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n5. Popularnost proizvoda po bojama")
    print(popularity_by_color)

# 3. Efikasnost prodaje

def analyze_top_5_efficient_brands(df):
    """ Pronalazi top 5 najefikasnijih brendova. """

    brand_stats = df.groupby("brand").agg({
        "quantity_sold": "sum",
        "quantity_in_stock": "sum"
    })

    # Nova kolona: ukupno nabavljeno
    
    brand_stats["total_quantity"] = (
        brand_stats["quantity_sold"] +
        brand_stats["quantity_in_stock"]
    )

    # Nova karakteristika: efikasnost prodaje

    brand_stats["sales_efficiency"] = (
        brand_stats["quantity_sold"] /
        brand_stats["total_quantity"]
    )

    top_5 = (
        brand_stats
        .sort_values(by="sales_efficiency", ascending=False)
        .head(5)
    )

    print("\n6. Top 5 najefikasnijih brendova po prodaji")
    print(top_5)


# Glavni deo programa

def main():
    analyze_product_ratings(df)
    analyze_most_common_brand(df)
    analyze_top_selling_brand(df)
    analyze_average_rating_by_category(df)
    analyze_popularity_by_color(df)
    analyze_top_5_efficient_brands(df)

if __name__ == "__main__":
    main()