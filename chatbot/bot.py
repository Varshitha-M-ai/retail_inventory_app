from agents.pricing_agent import get_price_suggestions
from agents.demand_agent import get_top_demand_products
from agents.store_agent import get_store_alerts
from agents.warehouse_agent import get_warehouse_status

def get_chat_response(query: str) -> str:
    try:
        import ollama
        response = ollama.chat(
            model='gemma:2b',
            messages=[{"role": "user", "content": query}]
        )
        content = response['message']['content']
        result = eval(content) if isinstance(content, str) and content.startswith("{") else {}

        # Route to agent functions if mapped
        if isinstance(result, dict) and "agent" in result:
            if result["agent"] == "pricing":
                return str(get_price_suggestions())
            elif result["agent"] == "demand":
                return str(get_top_demand_products())
            elif result["agent"] == "store":
                return str(get_store_alerts())
            elif result["agent"] == "warehouse":
                return str(get_warehouse_status())
            else:
                return "I recognized the intent but couldn't find a matching agent."
        
        # If not structured as dict, return raw content
        return content

    except Exception as e:
        return f"Sorry, I couldn't process your request. Error: {e}"
