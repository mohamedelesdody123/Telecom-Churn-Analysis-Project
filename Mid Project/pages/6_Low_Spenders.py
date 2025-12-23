import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Low Spenders", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    if 'spending_level' not in df.columns:
        df['spending_level'] = pd.qcut(df['total_charge'], q=3, labels=['Low', 'Medium', 'High'])
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("Low Spenders Analysis")
low_df = df[df['spending_level'] == 'Low']

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### Churn vs Usage")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(data=low_df, x='total_day_minutes', hue='churn_label', kde=True, palette=my_colors, element="step", ax=ax)
    st.pyplot(fig)
    st.write("Red curve is high at ZERO. They don't use the line.")

with c2:
    st.markdown("### General Churn")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.countplot(x='churn_label', data=low_df, palette=my_colors, ax=ax)
    st.pyplot(fig)
    st.write("This group is stable.")