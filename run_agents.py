from agents.demand_agent import get_top_demand_products
from agents.store_agent import get_store_alerts
from agents.warehouse_agent import get_warehouse_restock_plan
from agents.pricing_agent import get_pricing_recommendations

def run_all_agents():
    print("\n\U0001F4C8 Demand Forecasting:")
    demand = get_top_demand_products()
    for d in demand:
        print(f"  - Product ID: {d['Product ID']} → Demand Trend: {d['Demand Trend']}")

    print("\n\U0001F3EA Store Stock Alerts:")
    alerts = get_store_alerts()
    for a in alerts:
        print(f"  - Store {a['Store ID']} → Product {a['Product ID']} is below reorder point.")

    print("\n🏢 Warehouse Restocking Plan:")
    warehouse = get_warehouse_restock_plan()
    for w in warehouse:
        print(f"  - Product {w['Product ID']} → Restock {w['Restock Quantity']} units")

    print("\n📅 Pricing Recommendations:")
    pricing = get_pricing_recommendations()
    for p in pricing:
        print(f"  - Product {p['Product ID']} → Current: ₹{p['Current Price']} → Recommended: ₹{p['Recommended Price']}")

if __name__ == "__main__":
    run_all_agents()
