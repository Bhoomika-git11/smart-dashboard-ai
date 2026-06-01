from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_insight(analytics):
    prompt = f"""
    You are a senior business analyst.

    Given the following analytics data:
    - Trend: {analytics['trend']}
    - Sales drop percentage: {analytics['drop_percentage']}
    - Best region: {analytics['best_region']}
    - Worst region: {analytics['worst_region']}

    Write a clear, professional business insight with recommendations.
    Keep it concise and executive-friendly.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate business insights from data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
