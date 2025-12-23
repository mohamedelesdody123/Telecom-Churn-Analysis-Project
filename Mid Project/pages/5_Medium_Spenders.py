import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Medium Spenders", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    if 'spending_level' not in df.columns:
        df['spending_level'] = pd.qcut(df['total_charge'], q=3, labels=['Low', 'Medium', 'High'])
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("Medium Spenders Analysis")
med_df = df[df['spending_level'] == 'Medium']

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### The 5th Call Risk")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x='customer_service_calls', hue='churn_label', data=med_df, palette=my_colors, ax=ax)
    st.pyplot(fig)
    st.write("At call #5, they leave (50% risk).")

with c2:
    st.markdown("### Account Length")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.kdeplot(data=med_df, x='account_length', hue='churn_label', palette=my_colors, fill=True, ax=ax)
    st.pyplot(fig)
    st.write("Churn happens for new and old customers.")