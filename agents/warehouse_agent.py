import pandas as pd
import os

def get_warehouse_status():
    try:
        # Path to your inventory CSV
        csv_path = "./data/inventory_monitoring.csv"
        if not os.path.exists(csv_path):
            print("❌ inventory_monitoring.csv not found.")
            return []

        df = pd.read_csv(csv_path)

        # We'll assume warehouse status = Product ID and Stock Levels
        df_summary = df.groupby("Product ID")["Stock Levels"].sum().reset_index()

        return df_summary.to_dict(orient="records")

    except Exception as e:
        print(f"🔥 Error in get_warehouse_status: {e}")
        return []
