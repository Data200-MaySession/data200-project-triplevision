import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import missingno as msno

# -------------------------
# 🔧 Streamlit Page Setup
# -------------------------
st.set_page_config(page_title="Sleep Data Overview", layout="wide")
st.title("🛏️ Sleep & Lifestyle Data Overview")

# -------------------------
# 📥 Load Dataset
# -------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Data/student_sleep_patterns.csv")  # Adjust path as needed

df = load_data()

# -------------------------
# 🧾 Dataset Preview
# -------------------------
st.subheader("📌 Dataset Preview")
st.dataframe(df.head())

st.subheader("📈 Descriptive Statistics")
st.dataframe(df.describe(include="all").T)

# -------------------------
# 🧪 Chi-Squared Test Section
# -------------------------
st.subheader("🧪 Chi-Squared Test: Categorical Features vs Sleep Category")

# Create sleep category from Sleep_Duration
df["Sleep_Category"] = pd.qcut(df["Sleep_Duration"], q=3, labels=["Low", "Medium", "High"])

# Choose categorical columns automatically (object or category)
categorical_feats = df.select_dtypes(include=["object", "category"]).columns.tolist()

if categorical_feats:
    selected_feat = st.selectbox("Select a categorical feature", categorical_feats)

    # Prepare contingency table
    df[selected_feat] = df[selected_feat].astype("category")
    contingency = pd.crosstab(df[selected_feat], df["Sleep_Category"])
    st.markdown("### 📊 Contingency Table")
    st.dataframe(contingency)

    # Chi-Square test
    chi2, p, dof, expected = chi2_contingency(contingency)

    # Results
    st.markdown(f"""
    **Chi² Statistic**: {chi2:.4f}  
    **Degrees of Freedom**: {dof}  
    **p-value**: {p:.4e}  
    """)

    if p < 0.01:
        st.success("✅ Statistically significant relationship (p < 0.01)")
    else:
        st.info("ℹ️ No statistically significant relationship (p ≥ 0.01)")

    # Plot
    st.markdown(f"### 📉 Sleep Category Distribution by `{selected_feat}`")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x=selected_feat, hue="Sleep_Category", palette="Set2", ax=ax2)
    ax2.set_title(f"Sleep Category by {selected_feat}")
    st.pyplot(fig2)
else:
    st.warning("⚠️ No categorical features available for Chi-squared test.")

    