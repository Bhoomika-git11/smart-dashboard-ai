# 📊 Smart AI Dashboard – Automated Data Insights

An interactive AI-powered dashboard built with **Python and Streamlit** to visualize sales data, analyze regional performance, and generate automated AI-driven insights through API integration.

The project combines data visualization with AI-powered analysis to make business data easier to understand and support data-driven decision-making.

## 🚀 Features

- **Sales Data Visualization:** Display sales datasets in an interactive tabular format.
- **Regional Sales Analysis:** Visualize total sales across different regions using bar charts.
- **AI-Generated Insights:** Generate automated insights using an integrated backend API.
- **Interactive Dashboard:** Simple and user-friendly interface built with Streamlit.
- **API Integration:** Connect the dashboard frontend with a backend analysis service using HTTP requests.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive dashboard development |
| Pandas | Data loading and manipulation |
| Requests | Backend API communication |
| FastAPI | Backend API integration |
| Matplotlib / Streamlit Charts | Data visualization |

## 📂 Project Structure

```text
smart-dashboard-ai/
│
├── app.py
│
├── data/
│   └── sample_sales.csv
│
├── backend/
│   └── main.py
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/smart-dashboard-ai.git
```

**2. Navigate to the project directory**

```bash
cd smart-dashboard-ai
```

**3. Install dependencies**

```bash
pip install streamlit pandas requests fastapi uvicorn
```

**4. Start the backend API**

Run your FastAPI backend on port 8000.

```bash
uvicorn backend.main:app --reload --port 8000
```

**5. Run the Streamlit dashboard**

```bash
streamlit run app.py
```

## 📊 Dashboard Workflow

1. Load the sales dataset using Pandas.
2. Display the sales records in the dashboard.
3. Aggregate sales data by region.
4. Generate regional sales visualizations.
5. Click the **Generate AI Insights** button.
6. Fetch the analysis from the backend API.
7. Display the generated insights on the dashboard.

## 🎯 Project Objective

The primary objective of this project is to demonstrate how data analytics, interactive visualization, and AI-powered insights can be integrated into a single dashboard to simplify business analysis and improve decision-making.

## 🔮 Future Enhancements

- Add interactive filters for regions and sales categories.
- Integrate advanced machine learning models for sales forecasting.
- Add KPI cards for revenue, average sales, and growth.
- Implement automated report generation.
- Integrate more advanced LLM-based business insights.
- Add downloadable reports and dashboard exports.

## 👩‍💻 Author

**Bhoomika Takkar**

- [LinkedIn](https://linkedin.com/in/bhoomika11)
- [GitHub](https://github.com/Bhoomika-git11)
- [Portfolio](https://cosmic-coder-portfolio.vercel.app/)

---

⭐ If you find this project interesting, feel free to explore the repository!
