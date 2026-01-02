import pandas as pd

def load_clean_data(file_path):
    """
    Loads cleaned AI trends data from CSV file.
    """
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = load_clean_data("data/processed/ai_trends_cleaned.csv")
    print(df.head())