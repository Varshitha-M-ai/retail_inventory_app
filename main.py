from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.demand_agent import get_top_demand_products
from agents.pricing_agent import get_price_suggestions
from agents.store_agent import get_store_alerts
from agents.warehouse_agent import get_warehouse_status
from chatbot.bot import get_chat_response  # Uses Ollama now ✅



app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Retail Inventory Optimization API"}

@app.get("/insights/demand")
def demand_insights():
    return {"top_demand_products": get_top_demand_products()}

@app.get("/insights/pricing")
def pricing_insights():
    return {"price_suggestions": get_price_suggestions()}

@app.get("/insights/store")
def store_insights():
    return {"store_alerts": get_store_alerts()}

@app.get("/insights/warehouse")
def warehouse_insights():
    return {"warehouse_status": get_warehouse_status()}

@app.get("/chat")
def chatbot_response(query: str):
    return {"response": get_chat_response(query)}  # Real-time LLM response ✅
