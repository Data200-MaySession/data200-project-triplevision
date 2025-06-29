import streamlit as st
import pandas as pd
import pickle

# Load your trained regression pipeline model
with open("models/model_pipeline.pkl", "rb") as file:
    model_pipeline = pickle.load(file)

# Page config
st.set_page_config(
    page_title="Student Sleep Duration Predictor",
    page_icon="🛌",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🛏️ Student Sleep Duration Prediction")

st.markdown(
    """
    Predict a student's sleep duration based on their demographics and lifestyle factors.
    Use the sidebar to input student details, then click **Predict Sleep Duration**.
    """
)

# Sidebar inputs
st.sidebar.header("Student Details")

age = st.sidebar.slider("Age", 16, 35, 22)
gender = st.sidebar.selectbox("Gender", options=["Male", "Female", "Other"])
university_year = st.sidebar.selectbox("University Year", options=["1st Year", "2nd Year", "3rd Year", "4th Year"])
study_hours = st.sidebar.slider("Average Study Hours per Day", 0.0, 12.0, 6.0)
screen_time = st.sidebar.slider("Daily Screen Time (hours)", 0.0, 12.0, 3.0)
caffeine_intake = st.sidebar.number_input("Caffeine Intake (cups per day)", min_value=0, max_value=10, value=2)
physical_activity = st.sidebar.slider("Physical Activity (minutes per day)", 0, 180, 30)
sleep_quality = st.sidebar.slider("Sleep Quality (scale 1-10)", 1, 10, 7)

# Note: If your model uses weekday/weekend sleep start/end times, you can add those inputs similarly

# Prepare input DataFrame matching training features
input_df = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "University_Year": [university_year],
    "Study_Hours": [study_hours],
    "Screen_Time": [screen_time],
    "Caffeine_Intake": [caffeine_intake],
    "Physical_Activity": [physical_activity],
    "Sleep_Quality": [sleep_quality],
    # Add other features if needed, like "Weekday_Sleep_Start", etc.
})

# Prediction button
if st.sidebar.button("Predict Sleep Duration"):
    with st.spinner("Calculating..."):
        predicted_sleep = model_pipeline.predict(input_df)[0]

    st.subheader("Predicted Sleep Duration")
    st.success(f"🛌 Estimated Sleep Duration: {predicted_sleep:.2f} hours")

    # Show inputs for confirmation
    with st.expander("Input Details"):
        st.write(input_df.T)

st.markdown("---")
st.caption("Model trained on student sleep dataset with lifestyle and demographic features.")
