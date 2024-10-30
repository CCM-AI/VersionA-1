import streamlit as st
from datetime import datetime

# Placeholder functions for risk algorithms
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    return "High" if risk_score > 15 else "Moderate" if risk_score > 10 else "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 15 else "Low"

def calculate_copd_risk(smoking_years, age, fev1):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1)
    return "High" if risk_score > 25 else "Moderate" if risk_score > 15 else "Low"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1):
    risk_score = (frequency_of_symptoms * 2) + (nighttime_symptoms * 3) + (inhaler_use * 1.5) - (fev1 * 0.1)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 10 else "Low"

# AI Assistant Response with Objective References
def ai_assistant_response(query, results):
    response = ""
    high_risk_conditions = [condition for condition, risk in results.items() if risk == "High"]
    moderate_risk_conditions = [condition for condition, risk in results.items() if risk == "Moderate"]

    if "follow-up" in query.lower():
        response += "For high-risk cases, monthly check-ins are advised. Moderate-risk cases may require quarterly check-ups. "
        response += "Refer to American Heart Association and American Diabetes Association guidelines for specific recommendations."

    elif "monitoring" in query.lower():
        response += "For monitoring, high-risk conditions need daily self-checks. For cardiovascular risks, measure blood pressure daily; "
        if "Diabetes" in results:
            response += "high-risk diabetes patients should monitor fasting glucose daily. "
        response += "Review monitoring protocols per guidelines by the American College of Physicians."

    elif "self-management" in query.lower():
        response += "Patients should follow self-management practices such as the DASH diet for cardiovascular health or carbohydrate counting for diabetes. "
        response += "Adherence to medications and physical activity routines is essential across conditions."

    else:
        response += "I'm here to assist with questions on risk stratification, monitoring, self-management, and follow-up plans for chronic conditions."

    return response

# Initialize session state to store results
if 'results' not in st.session_state:
    st.session_state['results'] = {}

# Streamlit App Layout
st.title("Comprehensive Multi-Condition Risk Stratification, Care Plan, and AI Assistant")
st.write("This app assesses risk for chronic conditions, provides a unified care plan for multiple conditions, and includes an AI assistant for personalized queries.")

# Define tabs for each condition and the AI Assistant
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Cardiovascular Risk", "Diabetes Risk", "COPD Risk", "Asthma Risk", "Unified Care Plan", "AI Assistant"])

# Cardiovascular Risk Tab
with tab1:
    st.header("Cardiovascular Risk Assessment")
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    cholesterol = st.slider("Total Cholesterol (mg/dL)", 100, 300, 180)
    smoker = st.radio("Smoking Status", options=["Non-smoker", "Current smoker"])

    if st.button("Calculate Cardiovascular Risk"):
        cardio_risk = calculate_cardio_risk(age, systolic_bp, smoker == "Current smoker", cholesterol)
        st.write(f"**Cardiovascular Risk Level**: {cardio_risk}")
        st.session_state['results']["Cardiovascular"] = cardio_risk

# Diabetes Risk Tab
with tab2:
    st.header("Diabetes Risk Assessment")
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
    family_history = st.radio("Family History of Diabetes", options=["Yes", "No"])
    fasting_glucose = st.number_input("Fasting Glucose (mg/dL)", min_value=50, max_value=300, value=90)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1_copd = st.number_input("FEV1 (%) - COPD", min_value=20, max_value=100, value=80)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1_copd)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Asthma Symptoms (days per week)", 0, 7, 3)
    nighttime_symptoms = st.slider("Nighttime Symptoms (days per week)", 0, 7, 1)
    inhaler_use = st.slider("Inhaler Use (days per week)", 0, 7, 2)
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma)
        st.write(f"**Asthma Risk Level**: {asthma_risk}")
        st.session_state['results']["Asthma"] = asthma_risk

# Unified Care Plan Tab
with tab5:
    st.header("Unified Care Plan for Multi-Condition Management")

    # Display individual care plan for each condition with specific recommendations based on risk
    for condition, risk in st.session_state['results'].items():
        st.subheader(f"{condition} Care Plan (Risk Level: {risk})")
        if risk == "High":
            st.write(f"- **{condition}**: High-risk patients require aggressive intervention, close monitoring, and regular follow-up. Recommended steps include:")
            st.write("  - Frequent monitoring (daily or weekly)")
            st.write("  - Strict adherence to medications and lifestyle changes.")
            st.write("  - Monthly specialist consultations.")
        elif risk == "Moderate":
            st.write(f"- **{condition}**: Moderate-risk patients should follow a comprehensive management plan with regular monitoring and preventive measures:")
            st.write("  - Weekly to biweekly monitoring.")
            st.write("  - Consistent lifestyle adjustments (diet, exercise).")
            st.write("  - Quarterly primary care consultations.")
        else:
            st.write(f"- **{condition}**: Low-risk patients can maintain preventive measures to avoid escalation.")
            st.write("  - Annual health reviews.")
            st.write("  - Routine healthy lifestyle maintenance.")

# AI Assistant Tab
with tab6:
    st.header("AI Assistant for Healthcare Provider Guidance")
    query = st.text_input("Ask the AI Assistant about risk stratification, follow-up, monitoring, or self-management:")
    if st.button("Get AI Assistance"):
        if st.session_state['results']:
            ai_response = ai_assistant_response(query, st.session_state['results'])
            st.write(ai_response)
        else:
            st.write("Please complete risk assessments in previous tabs first.")
