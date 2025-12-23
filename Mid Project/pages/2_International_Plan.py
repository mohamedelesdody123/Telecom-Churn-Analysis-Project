import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="International", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("International Plan Analysis")
intl_users = df[df['international_plan'].isin(['yes', 'Yes', 1])]

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### Minutes vs Churn")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x='churn_label', y='total_intl_minutes', data=intl_users, palette=my_colors, errorbar=None, ax=ax)
    st.pyplot(fig)
    st.write("People talking MORE are leaving. Line quality is bad.")

with c2:
    st.markdown("### Charges Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(data=intl_users, x='total_intl_charge', hue='churn_label', kde=True, palette=my_colors, ax=ax)
    st.pyplot(fig)
    st.write("Higher charges = more churn here.")