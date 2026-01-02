import pandas as pd

def get_peak_interest(df):
    """
    Returns the row with maximum interest.
    """
    return df.loc[df['interest'].idxmax()]


def get_yearly_average(df):
    """
    Returns yearly average interest.
    """
    df['year'] = pd.to_datetime(df['date']).dt.year
    return df.groupby('year')['interest'].mean()


if __name__ == "__main__":
    df = pd.read_csv("data/processed/ai_trends_cleaned.csv")

    peak = get_peak_interest(df)
    yearly_avg = get_yearly_average(df)

    print("Peak Interest:")
    print(peak)

    print("\nYearly Average Interest:")
    print(yearly_avg)