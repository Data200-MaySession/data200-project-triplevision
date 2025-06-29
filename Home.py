import streamlit as st

st.set_page_config(
    page_title="Sleep Analysis App", 
    page_icon="😴", 
    layout="centered"
)

st.title("😴 Student Sleep Pattern Predictor")

st.markdown("""
Welcome to the **Sleep Duration Analysis App**!  
This tool explores how **lifestyle and academic factors** affect student sleep patterns using real data and machine learning.

---

### 🔍 What You Can Do Here:
- 📊 **Explore Data**: View statistics and visualizations of student behavior.
- 🧠 **Predict Sleep**: Input your lifestyle details to predict estimated sleep hours.
- 🧪 **Understand Influence**: See which habits most strongly affect sleep using feature importance analysis.

---

### 💡 Why This Matters
Poor sleep is linked to lower academic performance, stress, and health issues.  
This app helps you understand **what truly impacts your sleep** — and maybe even change it.

---

👤 **Project By**: *Triple Vision*  
📘 **Course**: DATA 200 – Applied Statistical Analysis  
""")
