import pandas as pd
import numpy as np

def generate_insights(df):
    insights = {}

    total_sales = df['sales'].sum()
    insights['total_sales'] = total_sales

    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['sales'].sum()
    growth = monthly_sales.pct_change().dropna()

    if len(growth) > 0 and growth.iloc[-1] < 0:
        insights['trend'] = "negative"
        insights['drop_percentage'] = round(abs(growth.iloc[-1] * 100), 2)
    else:
        insights['trend'] = "positive"
        insights['drop_percentage'] = 0

    region_sales = df.groupby('region')['sales'].sum()
    insights['best_region'] = region_sales.idxmax()
    insights['worst_region'] = region_sales.idxmin()

    return insights
