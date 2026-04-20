# 🏏 IPL Dashboard

> An interactive multi-category cricket analytics dashboard built with **Streamlit**, powered by **Pandas** — explore IPL Season 18 performance data with dynamic charts and player filters.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-≥1.32-FF4B4B?style=flat-square&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-≥2.0-150458?style=flat-square&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-≥5.20-3F4F75?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📖 About

The **IPL Dashboard** is a Streamlit web application that lets you browse, visualize, and filter IPL Season 18 performance datasets across 7 statistical categories — from batting runscorers to bowling economy leaders — all from a clean sidebar interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 Multi-category browser | Switch between 7 stat categories from the sidebar |
| 📁 Dynamic CSV loading | Auto-discovers all CSV files within each category folder |
| 📈 Bar chart visualization | Select any numeric column for an instant bar chart |
| 🔍 Player filter | Filter table rows by individual player |
| 🧹 Auto data cleaning | Strips unnamed index columns and trims whitespace from headers |
| ⚡ Cached reads | `@st.cache_data` speeds up repeated file loads |

---

## 🗂️ Data Categories

The dashboard supports the following 7 performance categories, each mapped to a subfolder containing season-wise CSV files:

1. **All Seasons Combined** — cross-season aggregated stats
2. **Most Runs** — top run-scorers per season
3. **Most Wickets** — top wicket-takers per season
4. **Fastest Fifties** — quickest fifty milestones
5. **Fastest Centuries** — quickest century milestones
6. **Best Bowling Economy Innings** — best economy rates in an innings
7. **Best Bowling Strike Rate Innings** — best strike rates in an innings

---

## 📁 Project Structure

```
project/
├── ipl_dashboard.py              ← Main Streamlit application
├── requirements.txt              ← Python dependencies
├── IPL18.ipynb                   ← Exploratory Data Analysis notebook
└── ipl 18/
    └── performance dataset/
        ├── All Seasons Combined/
        │   └── Most Runs All Seasons Combine.csv
        ├── Most Runs/
        ├── Most Wickets/
        ├── Fastest Fifties/
        ├── Fastest Centuries/
        ├── Best Bowling Economy Innings/
        └── Best Bowling Strike Rate Innings/
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourname/ipl-dashboard.git
cd ipl-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Place your datasets

Ensure your CSVs are structured as:

```
ipl 18/performance dataset/<Category Name>/<season>.csv
```

### 4. Run the app

```bash
streamlit run ipl_dashboard.py
```

Then open your browser at `http://localhost:8501`

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| [Streamlit](https://streamlit.io) | ≥ 1.32.0 | Web app framework & UI |
| [Pandas](https://pandas.pydata.org) | ≥ 2.0.0 | Data loading & manipulation |
| [Plotly](https://plotly.com/python) | ≥ 5.20.0 | Interactive charting |
| [NumPy](https://numpy.org) | ≥ 1.24.0 | Numerical operations |

---

## 🔍 How It Works

1. **Sidebar** lets the user pick a stat category and a specific season/file.
2. The selected CSV is loaded via `pd.read_csv()` with caching enabled.
3. Unnamed index columns are automatically dropped; column names are stripped.
4. **Raw data** is shown in a full-width `st.dataframe`.
5. **Summary stats** display row count, column count, and numeric column sum.
6. **Visualization** lets the user pick any numeric column and renders a bar chart.
7. If a `player` column exists, a **player filter** dropdown appears for row-level filtering.

---

## 📊 EDA Notebook

The included `IPL18.ipynb` notebook covers:

- Loading and inspecting the combined seasons dataset
- Checking for null values and duplicates
- Analysing player appearances across seasons
- Visualizing the top 50 players by seasons played (seaborn bar chart)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👤 Author

**Shivesh Verma**  
*Advanced IPL Dashboard · Season 18 Analytics*

---

> 🚀 *Built with passion for cricket and data.*
