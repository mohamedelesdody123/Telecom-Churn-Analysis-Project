import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Voice Mail", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    vm_col = [c for c in df.columns if 'voice' in c.lower() and 'plan' in c.lower()][0]
    df['has_voice_mail'] = df[vm_col].apply(lambda x: 'Yes' if str(x).lower() in ['yes', '1'] else 'No')
    return df

df = load_data()
my_colors = ["#2ecc71", "#e74c3c"]

st.title("Voice Mail Analysis")

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown("### Retention Power")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x='has_voice_mail', y='churn', data=df, palette="Blues", errorbar=None, ax=ax)
    ax.set_ylabel("Churn Probability")
    st.pyplot(fig)
    st.write("No Voice Mail = 2x Churn.")

with c2:
    st.markdown("### Messages Count")
    vm_users = df[df['has_voice_mail'] == 'Yes']
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(data=vm_users, x='number_vmail_messages', hue='churn_label', palette=my_colors, multiple="stack", ax=ax)
    st.pyplot(fig)
    st.write("Active VM users stay longer.")