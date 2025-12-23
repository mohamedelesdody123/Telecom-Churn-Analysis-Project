import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# setup page
st.set_page_config(page_title="Churn Analysis", layout="wide")

st.markdown("""
    <style>
    p {font-size: 16px !important;}
    </style>
    """, unsafe_allow_html=True)

# loading data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('cleaned_churn_data.csv')
    except:
        train = pd.read_csv('churn-bigml-80.csv')
        test = pd.read_csv('churn-bigml-20.csv')
        df = pd.concat([train, test], ignore_index=True)
        
    if 'spending_level' not in df.columns:
        df['spending_level'] = pd.qcut(df['total_charge'], q=3, labels=['Low', 'Medium', 'High'])
    
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.sidebar.title("Churn Project")
st.sidebar.write("By: **Mo Elesdody**")

st.title("Introduction: Project Overview")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Customers", f"{len(df)}")
with col2:
    st.metric("Total Left", f"{df['churn'].sum()}")
with col3:
    st.metric("Churn Rate", f"{df['churn'].mean()*100:.1f}%")

st.markdown("---")

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### Churn Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))
    df['churn_label'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, colors=my_colors, startangle=90)
    ax.set_ylabel('')
    st.pyplot(fig)
    st.write("Red slice is the problem. 14.5% is risky.")

with c2:
    st.markdown("### Charge Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(data=df, x='total_charge', hue='churn_label', kde=True, palette=my_colors, ax=ax)
    st.pyplot(fig)
    st.write("People paying more money are leaving more.")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("Start Analysis ➡️"):
    st.switch_page("pages/1_Location_Analysis.py")