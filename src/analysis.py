from pathlib import Path
import pandas as pd


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = PROJECT_ROOT / "data" / "food_orders.csv"


def load_data():
    """Load the food delivery dataset."""
    return pd.read_csv(DATA_PATH)


def basic_summary(df):
    """Display basic information about the dataset."""
    print("Dataset Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())


def delivery_time_summary(df):
    """Display delivery-time statistics."""
    delivery_time = df["Time_taken (min)"]

    print("\nDelivery Time Summary")
    print("---------------------")
    print(f"Average: {delivery_time.mean():.2f} minutes")
    print(f"Median: {delivery_time.median():.2f} minutes")
    print(f"Minimum: {delivery_time.min():.2f} minutes")
    print(f"Maximum: {delivery_time.max():.2f} minutes")


if __name__ == "__main__":
    df = load_data()

    basic_summary(df)
    delivery_time_summary(df)