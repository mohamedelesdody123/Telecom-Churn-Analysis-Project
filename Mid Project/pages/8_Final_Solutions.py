import streamlit as st

st.set_page_config(page_title="Solutions", layout="wide")

st.title("Final Solutions & Recommendations")

col1, _, col2 = st.columns([5, 0.5, 5])

with col1:
    st.subheader("Identified Problems")
    st.markdown("""
    **1. Network Coverage:**
    Poor signal in specific states.
    
    **2. International Plan:**
    Bad Voice Quality causes heavy users to leave.
    
    **3. High Spenders (VIPs):**
    They hate waiting for support.
    
    **4. Medium Spenders:**
    They leave after the 5th call.
    
    **5. Low Spenders:**
    Zero usage or better competitor offers.
    """)

with col2:
    st.subheader("Strategic Solutions")
    st.markdown("""
    **1. Fix The Network:**
    Send engineers to top bad states.
    
    **2. Improve Tech Quality:**
    Check international lines + Post-Call Feedback.
    
    **3. VIP Priority Lane:**
    Fast support line for VIPs.
    
    **4. Compensation:**
    If Medium spender calls 2 times, give free minutes. Stop the 5th call.
    
    **5. Win-Back Offers:**
    Budget deals for Low Spenders.
    
    **6. Free Voice Mail:**
    Since Voice Mail reduces churn by **50%**, make it a **FREE Feature** for all plans to increase customer loyalty.
    
    **7. Awareness & Propaganda (SMS):**
    Launch **SMS Campaigns** in fixed areas to announce improvements. Offer **Free Trials** so customers can test the new network quality themselves.
    """)

st.markdown("---")
st.markdown("<h3 style='text-align: center; color: grey;'>Analysis by: Mo Elesdody</h3>", unsafe_allow_html=True)