import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Location", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_churn_data.csv')
    df['churn_label'] = df['churn'].apply(lambda x: 'Left' if x == 1 else 'Stayed')
    return df

df = load_data()

st.title("Location Analysis (Network)")

top_n = st.slider("Select Number of States:", 5, 50, 5)

c1, _, c2 = st.columns([1, 0.1, 1])

with c1:
    st.markdown(f"### Top {top_n} Worst States")
    top_states = df.groupby('state')['churn'].mean().sort_values(ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x=top_states.index, y=top_states.values, palette="Reds_r", ax=ax)
    ax.set_ylabel("Churn Rate")
    st.pyplot(fig)
    st.write("High churn in these places = Bad Signal.")

with c2:
    st.markdown("### All States Ranked")
    all_states = df.groupby('state')['churn'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(5, 8))
    sns.barplot(x=all_states.values, y=all_states.index, palette="coolwarm_r", ax=ax)
    ax.set_xlabel("Churn Rate")
    st.pyplot(fig)

st.markdown("---")
st.markdown("### Geographic Heatmap")
churn_by_state = df.groupby('state')['churn'].mean().reset_index()
fig = px.choropleth(churn_by_state, locations='state', locationmode="USA-states", 
                    color='churn', scope="usa", color_continuous_scale="Reds")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=300)
st.plotly_chart(fig, use_container_width=True)