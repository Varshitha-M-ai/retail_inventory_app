# 🛍️ Retail Inventory Optimization App

A smart retail optimization system using multi-agent architecture and Gen AI (Gemma:2B via Ollama). It includes demand forecasting, dynamic pricing, warehouse management, and an intelligent chatbot.

## Tech Stack
- Streamlit (UI)
- FastAPI (Backend)
- Ollama (Gemma:2B model)
- Plotly (Charts)
- CSV-based data (Inventory, Demand, Pricing)

## How to Run

1. **Install dependencies**
   ```bash
    pip install -r requirements.txt

2. **Run Ollama with Gemma**
   ```bash
    ollama run gemma:2b

3. **Start FastAPI backend**
   ```bash
    uvicorn backend.main:app --reload

4. **Start Streamlit app**
   ```bash
    streamlit run ui/app.py

 **requirements.txt**
   ```bash
    streamlit
    fastapi
    uvicorn
    pandas
    plotly
    requests
    ollama

 **Code Structure**
   ```bash
   RETAIL_INVENTORY_APP/
├── agents/
│   ├── demand_agent.py
│   ├── pricing_agent.py
│   ├── store_agent.py
│   └── warehouse_agent.py
├── api/
│   └── main.py
├── chatbot/
│   └── bot.py
├── data/
│   ├── demand_forecasting.csv
│   ├── inventory_monitoring.csv
│   └── pricing_optimization.csv
├── ui/
│   └── app.py
├── utils/
│   └── database.py
├── requirements.txt








