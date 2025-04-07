import pandas as pd
import os

def get_top_demand_products():
    try:
        csv_path = "./data/demand_forecasting.csv"
        if not os.path.exists(csv_path):
            print("❌ demand_forecasting.csv not found at expected path")
            return []

        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()

        # Strip whitespace and normalize capitalization
        df["Demand Trend"] = df["Demand Trend"].str.strip().str.title()

        print("📊 Unique Demand Trend values before mapping:", df["Demand Trend"].unique())

        trend_map = {
            "Decreasing": -1,
            "Stable": 0,
            "Increasing": 1
        }
        df["Trend Score"] = df["Demand Trend"].map(trend_map)

        # Drop unmapped rows
        df = df.dropna(subset=["Trend Score"])

        grouped = df.groupby("Product ID", as_index=False)["Trend Score"].mean()
        top_demand = grouped.sort_values(by="Trend Score", ascending=False).head(10)

        # Rename for frontend chart
        top_demand.rename(columns={"Trend Score": "Demand Trend"}, inplace=True)

        return top_demand.to_dict(orient="records")

    except Exception as e:
        print(f"🔥 Error in get_top_demand_products: {e}")
        return []
