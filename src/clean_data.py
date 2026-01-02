import pandas as pd

def clean_ai_trends_data(df):
    """
    Cleans AI trends data:
    - Converts date column
    - Converts interest to numeric
    - Removes missing values
    """
    df.columns = ['date', 'interest']
    df['date'] = pd.to_datetime(df['date'])
    df['interest'] = pd.to_numeric(df['interest'], errors='coerce')
    df = df.dropna()
    df = df.reset_index(drop=True)
    return df


if __name__ == "__main__":
    raw_df = pd.read_csv("data/raw/google_trends_chatgpt_raw.csv", header=None)
    clean_df = clean_ai_trends_data(raw_df)
    clean_df.to_csv("data/processed/ai_trends_cleaned.csv", index=False)
    print("Data cleaned and saved successfully.")
