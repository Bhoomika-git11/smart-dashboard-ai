from fastapi import FastAPI
from data_processor import load_and_clean_data
from insight_engine import generate_insights
from gen_ai import generate_text_insight

app = FastAPI()

DATA_PATH = "data/sample_sales.csv"

@app.get("/analyze")
def analyze_data():
    df = load_and_clean_data(DATA_PATH)
    analytics = generate_insights(df)
    ai_insight = generate_text_insight(analytics)

    return {
        "analytics": analytics,
        "ai_insight": ai_insight
    }