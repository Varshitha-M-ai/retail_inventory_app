import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Retail Inventory Optimizer", layout="wide")
st.title("🛒 Retail Inventory Optimization Dashboard")

# Sidebar navigation
section = st.sidebar.radio("Navigate", ["📊 Insights", "💬 Chatbot"])

# --- Insights Dashboard ---
if section == "📊 Insights":
    st.header("Multi-Agent Insights Dashboard")

    # 🔹 Demand Forecasting
    st.subheader("📈 Top Demand Products")
    try:
        demand = requests.get(f"{API_URL}/insights/demand").json()["top_demand_products"]
        df_demand = pd.DataFrame(demand)

        # Convert demand trend back from numeric to label if needed
        if df_demand["Demand Trend"].dtype in [int, float]:
            df_demand["Demand Trend"] = df_demand["Demand Trend"].map({
                1: "Increasing",
                0: "Stable",
                -1: "Decreasing"
            })

        st.dataframe(df_demand)
    except Exception as e:
        st.error(f"Failed to fetch demand data: {e}")

    # 🔹 Pricing Recommendations
    st.subheader("💰 Pricing Suggestions")
    try:
        pricing = requests.get(f"{API_URL}/insights/pricing").json()["price_suggestions"]
        df_pricing = pd.DataFrame(pricing)
        if not df_pricing.empty:
            st.dataframe(df_pricing)
            fig_price = px.bar(df_pricing, x="Product ID", y="Suggested Price", title="Suggested New Prices")
            st.plotly_chart(fig_price, use_container_width=True)
        else:
            st.info("No pricing changes suggested at this time.")
    except Exception as e:
        st.error(f"Failed to fetch pricing suggestions: {e}")

    # 🔹 Warehouse Status
    st.subheader("📦 Warehouse Stock Status")
    try:
        warehouse = requests.get(f"{API_URL}/insights/warehouse").json()["warehouse_status"]
        df_warehouse = pd.DataFrame(warehouse)
        st.dataframe(df_warehouse)
        fig_warehouse = px.pie(df_warehouse, names="Product ID", values="Stock Levels", title="Warehouse Stock Distribution")
        st.plotly_chart(fig_warehouse, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to fetch warehouse stock status: {e}")

    # 🏬 Store Alerts
    st.subheader("🏬 Store Stock Alerts")
    try:
        store = requests.get(f"{API_URL}/insights/store").json()["store_alerts"]
        df_store = pd.DataFrame(store)
        if not df_store.empty:
            st.dataframe(df_store)
        else:
            st.success("All stores have healthy stock levels.")
    except Exception as e:
        st.error(f"Failed to fetch store alerts: {e}")

# --- Chatbot Section ---
elif section == "💬 Chatbot":
    st.header("💬 Ask Our Retail AI Assistant")

    user_input = st.text_input("Type your question:")
    if st.button("Ask"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                try:
                    response = requests.get(f"{API_URL}/chat", params={"query": user_input})
                    if response.status_code == 200:
                        result = response.json()
                        st.markdown(f"**Assistant:** {result.get('response', 'No response')}**")
                    else:
                        st.error("Failed to get a valid response from the chatbot.")
                except Exception as e:
                    st.error(f"Chatbot error: {e}")
        else:
            st.warning("Please enter a question.")
