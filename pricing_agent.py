import pandas as pd

def get_price_suggestions():
    df = pd.read_csv("./data/pricing_optimization.csv")

    # Simple logic: if competitor price is lower, suggest reducing by 5%
    suggestions = []
    for _, row in df.iterrows():
        if row["Competitor Prices"] < row["Price"]:
            new_price = row["Competitor Prices"] * 0.95
            suggestions.append({
                "Product ID": row["Product ID"],
                "Store ID": row["Store ID"],
                "Current Price": row["Price"],
                "Suggested Price": round(new_price, 2),
                "Reason": "Competitor offers lower price"
            })

    return suggestions
