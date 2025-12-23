import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Segmentation", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    df['cost_per_min'] = df['total_day_charge'] / df['total_day_minutes'].replace(0, 1)
    if 'spending_level' not in df.columns:
        df['spending_level'] = pd.qcut(df['total_charge'], q=3, labels=['Low', 'Medium', 'High'])
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("Customer Segmentation Strategy")
st.markdown("### Is Money the Problem?")

c1, c2 = st.columns(2)

with c1:
    st.write("**1. Distribution Curves (KDE)**")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.kdeplot(data=df, x='cost_per_min', hue='churn_label', palette=my_colors, fill=True, ax=ax)
    ax.set_xlabel("Cost Per Minute ($)")
    st.pyplot(fig)

with c2:
    st.write("**2. Side-by-Side Columns**")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(data=df, x='cost_per_min', hue='churn_label', multiple="dodge", palette=my_colors, bins=15, ax=ax)
    ax.set_xlabel("Cost Per Minute ($)")
    st.pyplot(fig)

st.success("Proof: Both groups pay the same rates. Price is NOT the problem.")

st.markdown("---")
st.markdown("### Segmentation Logic")
st.write("Dividing customers by Bill Size:")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("**High Spenders (VIPs)**")
with col2:
    st.warning("**Medium Spenders**")
with col3:
    st.success("**Low Spenders**")

st.markdown("### Groups Distribution")
fig, ax = plt.subplots(figsize=(6, 3))
sns.countplot(x='spending_level', data=df, palette="viridis", ax=ax)
st.pyplot(fig)