import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="VIPs", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    if 'spending_level' not in df.columns:
        df['spending_level'] = pd.qcut(df['total_charge'], q=3, labels=['Low', 'Medium', 'High'])
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("High Spenders (VIP Analysis)")
vip_df = df[df['spending_level'] == 'High']

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### Customer Service Calls")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x='customer_service_calls', hue='churn_label', data=vip_df, palette=my_colors, ax=ax)
    st.pyplot(fig)
    st.write("VIPs leave fast if support is bad.")

with c2:
    st.markdown("### Usage Intensity")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.scatterplot(x='total_day_minutes', y='total_eve_minutes', hue='churn_label', data=vip_df, palette=my_colors, alpha=0.6, ax=ax)
    st.pyplot(fig)
    st.write("Heavy users are leaving too.")