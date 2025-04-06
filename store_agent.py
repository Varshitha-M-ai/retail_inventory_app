import pandas as pd

def get_store_alerts():
    df = pd.read_csv("data/inventory_monitoring.csv")
    df_alerts = df[df["Stock Levels"] < df["Reorder Point"]]
    return df_alerts[["Product ID", "Store ID", "Stock Levels", "Reorder Point"]].to_dict(orient="records")
