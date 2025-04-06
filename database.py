import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_demand_data():
    path = os.path.join(DATA_DIR, 'demand_forecasting.csv')
    return pd.read_csv(path)

def load_inventory_data():
    path = os.path.join(DATA_DIR, 'inventory_monitoring.csv')
    return pd.read_csv(path)

def load_pricing_data():
    path = os.path.join(DATA_DIR, 'pricing_optimization.csv')
    return pd.read_csv(path)
