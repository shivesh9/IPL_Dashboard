import streamlit as st
import pandas as pd
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="IPL Dashboard", layout="wide")

DATA_PATH = "ipl 18\\performance dataset"

# ---------------- FUNCTIONS ----------------
@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)

def get_files(folder):
    path = os.path.join(DATA_PATH, folder)
    files = [f for f in os.listdir(path) if f.endswith(".csv")]
    return files, path

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏏 IPL Dashboard")

category = st.sidebar.selectbox(
    "Select Category",
    [
        "All Seasons Combined",
        "Most Runs",
        "Most Wickets",
        "Fastest Fifties",
        "Fastest Centuries",
        "Best Bowling Economy Innings",
        "Best Bowling Strike Rate Innings"
    ]
)

# ---------------- LOAD FILES ----------------
files, folder_path = get_files(category)

# Remove .csv for display
display_files = [f.replace(".csv", "") for f in files]

selected_display = st.sidebar.selectbox("Select Season/File", display_files)

# Map back to original filename
selected_file = files[display_files.index(selected_display)]

file_path = os.path.join(folder_path, selected_file)
df = load_csv(file_path)

# ✅ FIX 1: REMOVE "Unnamed: 0"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# ✅ FIX 2: CLEAN COLUMN NAMES
df.columns = df.columns.str.strip()

# ---------------- MAIN UI ----------------
st.title(f"📊 {category} Dashboard")

st.subheader("📄 Raw Data")
st.dataframe(df, use_container_width=True)

# ---------------- BASIC STATS ----------------
st.subheader("📈 Summary Stats")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

if df.select_dtypes(include='number').shape[1] > 0:
    col3.metric("Total (Numeric Sum)", int(df.select_dtypes(include='number').sum().sum()))

# ---------------- VISUALIZATION ----------------
st.subheader("📊 Visualization")

numeric_cols = [
    col for col in df.select_dtypes(include='number').columns
    if "unnamed" not in col.lower()
]

if len(numeric_cols) > 0:
    selected_col = st.selectbox("Select Numeric Column", numeric_cols)

    clean_df = df[[selected_col]].copy()
    clean_df[selected_col] = pd.to_numeric(clean_df[selected_col], errors='coerce')
    clean_df = clean_df.dropna()

    if clean_df.empty:
        st.warning("No valid data to display.")
    else:
        st.bar_chart(clean_df)

else:
    st.warning("No numeric columns found for visualization.")

# ---------------- PLAYER FILTER ----------------
if 'player' in df.columns:
    st.subheader("🔍 Player Filter")
    player = st.selectbox("Select Player", df['player'].unique())
    st.dataframe(df[df['player'] == player])

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("🚀 Advanced IPL Dashboard by Shivesh Verma")