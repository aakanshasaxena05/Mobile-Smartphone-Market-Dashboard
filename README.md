# 📱 Mobile & Smartphone Market Dashboard

An interactive and visually engaging **Mobile & Smartphone Market Dashboard** developed using **Python, Streamlit, Pandas, and Plotly**.

This project is designed to analyze and visualize smartphone market data for both the **Indian and Global smartphone markets**. The dashboard converts market data into interactive charts, KPI cards, comparisons, and trend visualizations, making complex market information easier to understand.

The dashboard focuses on important business and market metrics such as **smartphone shipments, market share, brand performance, year-over-year (YoY) changes, shipment distribution, and quarterly trends**.

---

## 📌 Project Overview

The smartphone industry is highly competitive, with multiple brands competing across different markets and price segments. Understanding shipment volumes and market share can help users identify market trends and compare the performance of major smartphone vendors.

This project provides an interactive dashboard where users can switch between **India** and **Global** markets and explore different aspects of smartphone market performance.

Instead of presenting the information only through static tables, the project uses interactive visualizations to make the analysis more intuitive and user-friendly.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To analyze smartphone shipment data.
* To compare the market share of major smartphone brands.
* To visualize India and global smartphone markets.
* To analyze vendor performance.
* To understand year-over-year shipment changes.
* To identify changes in market share over time.
* To present important market metrics through KPI cards.
* To create an interactive and professional business dashboard.
* To demonstrate practical data-analysis and visualization skills using Python.

---

# 🚀 Features

## 📊 1. Interactive Market Share Analysis

The dashboard provides interactive market-share visualizations that allow users to compare smartphone brands.

Users can easily identify how much of the market each major smartphone vendor represents within the selected market.

The dashboard provides separate views for:

* 🇮🇳 India
* 🌍 Global Market

---

## 📱 2. Smartphone Brand Comparison

The dashboard allows users to compare major smartphone brands based on shipment performance.

Brands included in the analysis include:

### India Market

* vivo
* Samsung
* OPPO
* Xiaomi
* Apple
* Others

### Global Market

* Samsung
* Apple
* Xiaomi
* OPPO
* vivo
* Others

This makes it easier to understand differences between the Indian and global smartphone markets.

---

## 🇮🇳 3. India Smartphone Market Analysis

The India section focuses on smartphone shipment performance within the Indian market.

Users can explore:

* Brand market share
* Shipment volumes
* Vendor comparison
* Quarterly trends
* Top brands
* Shipment distribution

The dashboard provides an easy way to understand how different smartphone brands perform within India's competitive smartphone market.

---

## 🌍 4. Global Smartphone Market Analysis

The global section provides a broader view of smartphone shipments and vendor performance.

Users can analyze:

* Global shipment volumes
* Global market share
* Brand comparison
* Year-over-year changes
* Vendor performance
* Shipment distribution

The global view helps users compare the performance of major smartphone manufacturers at an international level.

---

## 📈 5. Vendor Shipment Trend Visualization

The dashboard includes trend visualizations that show how smartphone vendors' market shares change over time.

The India trend section uses quarterly data to visualize vendor performance.

Users can observe changes across:

```text
Q1 2025
Q2 2025
Q3 2025
Q4 2025
Q1 2026
Q2 2026
```

This makes it easier to understand whether a brand's shipment share has increased, decreased, or remained relatively stable.

---

## 🔄 6. Year-over-Year (YoY) Performance Analysis

The global dashboard includes a YoY shipment-change analysis.

This allows users to compare current shipment performance against the previous year's corresponding period.

The analysis helps highlight:

* Positive shipment growth
* Shipment decline
* Differences between vendors
* Overall market pressure

The visualization makes it easier to compare vendor performance without manually calculating percentage changes.

---

## 🎯 7. KPI Cards

The dashboard includes KPI cards that summarize important market information.

Depending on the selected market, users can see metrics such as:

### Total Q2 2026 Shipments

Shows the total smartphone shipments for the selected market.

### Market Leader

Displays the vendor with the highest shipment share in the selected dataset.

### Top-2 Combined Share

Shows the combined shipment share of the top two vendors.

### Highest YoY Growth

For the global market, this identifies the vendor with the highest reported YoY shipment growth.

For the India market, the dashboard displays the Top-5 market share instead.

---

## 🥧 8. Shipment Mix Visualization

A donut chart is used to display the shipment distribution among smartphone vendors.

The visualization provides a quick understanding of how total smartphone shipments are distributed across brands.

Users can hover over the chart to inspect individual vendor values.

---

## 📋 9. Detailed Vendor Data Table

The dashboard includes a detailed table containing vendor-level market information.

The table can display information such as:

* Brand
* Shipment volume
* Market share
* YoY change

This allows users to examine the underlying values behind the visualizations.

---

## 🎛️ 10. Interactive Market Selector

A sidebar selector allows users to switch between:

```text
🇮🇳 India
🌍 Global
```

When the market selection changes, the dashboard automatically updates the:

* KPI cards
* Market-share chart
* Shipment-mix chart
* Vendor performance chart
* Detailed vendor table

This makes the dashboard interactive rather than static.

---

## 💻 11. Responsive Streamlit Dashboard

The dashboard is built using **Streamlit**, which allows the Python-based analysis to be presented as an interactive web application.

The layout uses:

* Sidebar controls
* KPI cards
* Multiple chart sections
* Interactive tables
* Responsive columns
* Custom CSS styling

---

## 🎨 12. Professional Dashboard UI

The project uses custom styling to create a clean and professional interface.

The dashboard includes:

* Modern header section
* KPI cards
* Professional typography
* Structured sections
* Consistent spacing
* Interactive charts
* Clean tables
* Responsive layout

The goal is to make the dashboard suitable for a **data analytics portfolio or GitHub project**.

---

# 🛠️ Technologies Used

The project is developed using the following technologies:

### 🐍 Python

Python is used as the primary programming language for implementing the dashboard logic and data processing.

### 🎈 Streamlit

Streamlit is used to create the interactive web dashboard directly from Python.

### 🐼 Pandas

Pandas is used for:

* Creating DataFrames
* Organizing market data
* Data manipulation
* Data transformation
* Preparing data for visualization

### 📊 Plotly

Plotly is used for interactive visualizations such as:

* Bar charts
* Donut charts
* Line charts
* Market-share comparisons
* Vendor performance analysis

### 🎨 HTML & CSS

Custom HTML and CSS styling are used to improve the dashboard's visual appearance and create a professional UI.

---

# 📂 Project Structure

```text
Mobile-Smartphone-Market-Dashboard/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the complete Streamlit dashboard application, including:

* Data
* Dashboard layout
* KPI calculations
* Filters
* Charts
* Tables
* Styling

### `requirements.txt`

Contains the Python libraries required to run the dashboard.

### `README.md`

Contains project documentation, installation instructions, features, and usage information.

---

# ⚙️ Installation & Setup

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Mobile-Smartphone-Market-Dashboard.git
```

---

## Step 2: Navigate to the Project Directory

```bash
cd Mobile-Smartphone-Market-Dashboard
```

---

## Step 3: Install Required Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local URL where the dashboard can be opened in a web browser.

Usually:

```text
http://localhost:8501
```

---

# 📦 Requirements

The `requirements.txt` file should contain:

```text
streamlit
pandas
plotly
```

---

# 📊 Dashboard Workflow

The dashboard follows a simple analytical workflow:

```text
Market Data
     ↓
Data Preparation
     ↓
Market Selection
     ↓
KPI Calculation
     ↓
Data Visualization
     ↓
Vendor Comparison
     ↓
Trend Analysis
     ↓
Business Insights
```

---

# 🔍 How to Use the Dashboard

### Step 1

Launch the Streamlit application.

### Step 2

Use the sidebar to select the desired market:

* India
* Global

### Step 3

Review the KPI cards at the top of the dashboard.

### Step 4

Analyze the market-share visualization.

### Step 5

Explore the shipment-mix donut chart.

### Step 6

Use the vendor performance chart to compare brands.

### Step 7

Review the quarterly trend visualization.

### Step 8

Use the detailed vendor table to inspect the underlying data.

---

# 📈 Key Metrics

The dashboard focuses on the following metrics:

| Metric             | Description                            |
| ------------------ | -------------------------------------- |
| Shipments          | Number of smartphones shipped          |
| Market Share       | Vendor's share of total shipments      |
| YoY Change         | Year-over-year shipment change         |
| Top-2 Share        | Combined share of the top two vendors  |
| Top-5 Share        | Combined share of the top five vendors |
| Vendor Performance | Comparison between smartphone brands   |

---

# 🌐 Markets Covered

## 🇮🇳 India

The India dashboard focuses on Q2 2026 smartphone shipments and quarterly vendor-share trends.

Major vendors included:

```text
vivo
Samsung
OPPO
Xiaomi
Apple
Others
```

## 🌍 Global

The global dashboard focuses on Q2 2026 worldwide smartphone shipments and vendor YoY performance.

Major vendors included:

```text
Samsung
Apple
Xiaomi
OPPO
vivo
Others
```

---

# 📚 Data Sources

The dashboard uses published smartphone market research data from industry research organizations, including:

* **Omdia**
* **IDC**

The dashboard uses shipment-based market data.

> **Important:** Smartphone shipment share should not be interpreted as installed-base share, active-user share, or smartphone usage share.

---

# 💡 Business Use Cases

This dashboard can be useful for:

* 📊 Market research
* 📈 Business analysis
* 📱 Smartphone industry analysis
* 🏢 Competitive analysis
* 🎓 Academic projects
* 💼 Data analytics portfolios
* 📑 Business presentations
* 📉 Market trend analysis

---

# 🧠 Data Analytics Skills Demonstrated

This project demonstrates practical skills in:

* Data analysis
* Data visualization
* Python programming
* Pandas DataFrames
* Data transformation
* KPI development
* Market-share calculations
* Percentage analysis
* Trend analysis
* Business intelligence
* Dashboard development
* Interactive visualization
* Streamlit application development

---

# 🎓 Learning Outcomes

Through this project, the following concepts can be practiced:

1. Building an interactive dashboard using Streamlit.
2. Working with structured market datasets.
3. Creating DataFrames using Pandas.
4. Performing basic data aggregation.
5. Creating KPI metrics.
6. Creating interactive Plotly charts.
7. Comparing multiple categories.
8. Analyzing time-series trends.
9. Creating a professional dashboard interface.
10. Presenting data-driven insights visually.

---

# 🔮 Future Improvements

The project can be extended with additional functionality such as:

* 📅 Multi-year historical analysis
* 🌎 Country-wise market comparison
* 💰 Smartphone price-segment analysis
* 📱 Premium vs budget smartphone analysis
* 🏷️ Brand-wise price analysis
* 📈 Forecasting and predictive analytics
* 🔎 Advanced dashboard filters
* 📥 CSV/Excel data upload
* 📤 Downloadable reports
* 🔗 API-based live data
* 🗄️ Database integration
* ☁️ Streamlit Cloud deployment
* 📊 Additional interactive Plotly charts

---

# 🚀 Future Scope

A future version of this project could integrate a live or regularly updated data source so that the dashboard automatically refreshes with new smartphone market information.

Machine-learning models could also be added to analyze historical trends and create demand or shipment forecasts.

---

# ⚠️ Disclaimer

This project is created for **educational, analytical, and portfolio purposes**.

The market figures displayed in the dashboard are based on published shipment estimates from the referenced research sources. Different research organizations may report different figures because of differences in methodology, coverage, timing, and estimation.

Therefore, the dashboard should be used as a visualization and analysis project rather than as an official financial or investment recommendation.

---



Interested in:

* Python
* Data Analytics
* Data Visualization
* Dashboard Development
* Salesforce
* Technology

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ **Star** on GitHub.

You can also fork the repository and extend the dashboard with your own datasets and visualizations.

---

## 📌 Project Summary

**Mobile & Smartphone Market Dashboard** is a Python-based interactive analytics project that transforms smartphone shipment data into an easy-to-understand visual dashboard.

It combines **data analysis, interactive visualization, business intelligence, and Streamlit development** to provide a clear view of smartphone vendor performance in the **India and Global markets**.

# 👩‍💻 Author

## Aakansha Saxena
