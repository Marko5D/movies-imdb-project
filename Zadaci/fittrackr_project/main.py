import pandas as pd


def load_and_clean_data(file_path):
    """Ucitavanje i pretprocesiranje podataka"""

    df = pd.read_csv(file_path)

    # Ekstrahovanje brojeva iz Duration kolone
    df["Duration"] = df["Duration"].str.replace(" min", "", regex=False)
    df["Duration"] = pd.to_numeric(df["Duration"], errors="coerce")

    # Ekstrahovanje brojeva iz Calories kolone
    df["Calories"] = df["Calories"].str.replace(" kcal", "", regex=False)
    df["Calories"] = pd.to_numeric(df["Calories"], errors="coerce")

    # Uklanjanje potpunih duplikata
    df = df.drop_duplicates()

    # Uklanjanje redova bez korisnika
    df = df.dropna(subset=["Username"], how="all")

    # Standardizacija Activity kolone
    df["Activity"] = df["Activity"].str.lower().str.strip()

    df["Activity"] = df["Activity"].replace({
        "walk": "walking",
        "run": "running",
        "cycle": "cycling",
        "bike": "cycling",
        "yoga ": "yoga"
    })

    return df


def analyze_data(df):
    """Analiza ociscenih podataka"""

    print("\n--- ANALIZA FITTRACKR PODATAKA ---")

    average_duration = df["Duration"].mean()
    print("\n1. Prosecno trajanje aktivnosti:")
    print(round(average_duration, 2), "min")

    most_common_mood = df["Mood"].mode()[0]
    print("\n2. Najcesce raspolozenje korisnika nakon aktivnosti:")
    print(most_common_mood)

    calories_std = df["Calories"].std()
    print("\n3. Varijacija broja potrosenih kalorija:")
    print(round(calories_std, 2), "kcal")

    q1 = df["Age"].quantile(0.25)
    q3 = df["Age"].quantile(0.75)
    iqr = q3 - q1

    print("\n4. Razlika u godinama izmedju sredisnjih 50% korisnika:")
    print(iqr)


def main():
    file_path = "fit_trackr_data.csv"

    df = load_and_clean_data(file_path)
    analyze_data(df)


if __name__ == "__main__":
    main()