import streamlit as st
from datetime import datetime

# Placeholder functions for risk algorithms (using general guidelines for stratification)
def calculate_cardio_risk(age, systolic_bp, smoker, cholesterol):
    risk_score = (age * 0.1) + (systolic_bp * 0.05) + (10 if smoker else 0) + (cholesterol * 0.02)
    return "High" if risk_score > 15 else "Moderate" if risk_score > 10 else "Low"

def calculate_diabetes_risk(bmi, age, family_history, fasting_glucose, hba1c):
    risk_score = (bmi * 0.3) + (age * 0.1) + (10 if family_history else 0) + (fasting_glucose * 0.02) + (hba1c * 0.1)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 15 else "Low"

def calculate_copd_risk(smoking_years, age, fev1, exacerbations_last_year):
    risk_score = (smoking_years * 0.5) + (age * 0.2) - (fev1 * 0.1) + (exacerbations_last_year * 5)
    return "High" if risk_score > 25 else "Moderate" if risk_score > 15 else "Low"

def calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1, eosinophil_count):
    risk_score = (frequency_of_symptoms * 2) + (nighttime_symptoms * 3) + (inhaler_use * 1.5) - (fev1 * 0.1) + (eosinophil_count * 0.2)
    return "High" if risk_score > 20 else "Moderate" if risk_score > 10 else "Low"

# AI Assistant Response with Objective References
def ai_assistant_response(query, results):
    response = ""
    high_risk_conditions = [condition for condition, risk in results.items() if risk == "High"]
    moderate_risk_conditions = [condition for condition, risk in results.items() if risk == "Moderate"]

    if "follow-up" in query.lower():
        response += "For high-risk cases, guidelines recommend close monitoring and follow-ups as per condition:\n"
        if "Cardiovascular" in results:
            response += "- **Cardiovascular**: Monthly blood pressure checks and bi-annual lipid profiles. Consider frequent ECGs for high-risk patients.\n"
        if "Diabetes" in results:
            response += "- **Diabetes**: Quarterly HbA1c checks and monthly blood glucose monitoring. Emphasize diabetic foot exams.\n"
        if "COPD" in results:
            response += "- **COPD**: Regular spirometry every 3-6 months and biannual respiratory checkups. High-risk patients may benefit from pulmonary rehab.\n"
        if "Asthma" in results:
            response += "- **Asthma**: Spirometry every 6 months and close follow-up for medication adherence and asthma action plan updates.\n"
        response += "Refer to respective guidelines (e.g., AHA, ADA) for specific protocols."

    elif "monitoring" in query.lower():
        response += "Monitoring protocols by condition:\n"
        if "Cardiovascular" in results:
            response += "- **Cardiovascular**: Daily BP logging, weekly weight checks. For high-risk, lipid panels every 3 months.\n"
        if "Diabetes" in results:
            response += "- **Diabetes**: Daily glucose monitoring, quarterly HbA1c. Routine kidney and eye exams yearly.\n"
        if "COPD" in results:
            response += "- **COPD**: Track symptoms daily, spirometry every 3-6 months, and monitor oxygen saturation if needed.\n"
        if "Asthma" in results:
            response += "- **Asthma**: Peak flow monitoring daily for high-risk, symptom diary, and annual allergen testing.\n"
        response += "Monitoring should adhere to standards set by leading health organizations."

    elif "self-management" in query.lower():
        response += "Encourage self-management:\n"
        if "Cardiovascular" in results:
            response += "- **Cardiovascular**: Promote DASH diet, 30 min daily exercise, and stress reduction. Smoking cessation is critical.\n"
        if "Diabetes" in results:
            response += "- **Diabetes**: Carbohydrate counting, regular meal planning, and physical activity (150 min/week).\n"
        if "COPD" in results:
            response += "- **COPD**: Smoking cessation, breathing exercises, and pulmonary rehab.\n"
        if "Asthma" in results:
            response += "- **Asthma**: Action plan adherence, allergen avoidance, and inhaler technique training.\n"
        response += "Tailor recommendations per American Diabetes Association, NIH, and CDC guidelines."

    else:
        response += "I'm here to assist with evidence-based follow-up, monitoring, and self-management protocols. Please ask about specific condition management."

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
    hba1c = st.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=5.6)

    if st.button("Calculate Diabetes Risk"):
        diabetes_risk = calculate_diabetes_risk(bmi, age, family_history == "Yes", fasting_glucose, hba1c)
        st.write(f"**Diabetes Risk Level**: {diabetes_risk}")
        st.session_state['results']["Diabetes"] = diabetes_risk

# COPD Risk Tab
with tab3:
    st.header("COPD Risk Assessment")
    smoking_years = st.number_input("Years of Smoking (if applicable)", min_value=0, max_value=60, value=0)
    fev1_copd = st.number_input("FEV1 (%) - COPD", min_value=20, max_value=100, value=80)
    exacerbations_last_year = st.number_input("Number of COPD Exacerbations in Last Year", min_value=0, max_value=10, value=0)

    if st.button("Calculate COPD Risk"):
        copd_risk = calculate_copd_risk(smoking_years, age, fev1_copd, exacerbations_last_year)
        st.write(f"**COPD Risk Level**: {copd_risk}")
        st.session_state['results']["COPD"] = copd_risk

# Asthma Risk Tab
with tab4:
    st.header("Asthma Risk Assessment")
    frequency_of_symptoms = st.slider("Frequency of Asthma Symptoms (days per week)", 0, 7, 3)
    nighttime_symptoms = st.slider("Nighttime Symptoms (days per week)", 0, 7, 1)
    inhaler_use = st.slider("Inhaler Use (days per week)", 0, 7, 2)
    fev1_asthma = st.number_input("FEV1 (%) - Asthma", min_value=20, max_value=100, value=80)
    eosinophil_count = st.number_input("Eosinophil Count (cells/μL)", min_value=0, max_value=1500, value=300)

    if st.button("Calculate Asthma Risk"):
        asthma_risk = calculate_asthma_risk(frequency_of_symptoms, nighttime_symptoms, inhaler_use, fev1_asthma, eosinophil_count)
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
