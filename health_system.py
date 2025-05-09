
import streamlit as st

st.set_page_config(page_title="AI Health Checker", page_icon="🧬")
st.title("👀Health Checker")
st.subheader("Input your details to get personalized health feedback.")

# User Info
name = st.text_input("Name:")
age = st.number_input("Age:", min_value=0, max_value=120, step=1)
gender = st.radio("Gender:", ["Male", "Female"])

# Health Inputs
blood_pressure = st.number_input("Blood Pressure (systolic):")
fasting_blood_sugar = st.number_input("Fasting Blood Sugar:")
random_blood_sugar = st.number_input("Random Blood Sugar:")
heart_rate = st.number_input("Heart Rate:")
temperature = st.number_input("Body Temperature (°C):")

# Basic rule-based logic for health checks
if st.button("Analyze Health"):
    st.markdown(f"### Health Report for **{name}**")

    # Blood Pressure Check
    bp_status = ""
    if 14 < age <= 18:
        if blood_pressure < 90:
            bp_status = "Blood pressure is low."
        elif 90 <= blood_pressure <= 120:
            bp_status = "Blood pressure is normal."
        else:
            bp_status = "Blood pressure is high."
    elif 19 <= age <= 40:
        if blood_pressure < 95:
            bp_status = "Blood pressure is low."
        elif 95 <= blood_pressure <= 135:
            bp_status = "Blood pressure is normal."
        else:
            bp_status = "Blood pressure is high."
    elif 41 <= age <= 60:
        if blood_pressure < 110:
            bp_status = "Blood pressure is low."
        elif 110 <= blood_pressure <= 145:
            bp_status = "Blood pressure is normal."
        else:
            bp_status = "Blood pressure is high."
    elif age > 60:
        if blood_pressure < 95:
            bp_status = "Blood pressure is low."
        elif 95 <= blood_pressure <= 145:
            bp_status = "Blood pressure is normal."
        else:
            bp_status = "Blood pressure is high."
    st.markdown(f"**Blood Pressure:** {bp_status}")

    # Fasting Blood Sugar Check
    fasting_sugar_status = ""
    if age <= 3:
        if fasting_blood_sugar < 60:
            fasting_sugar_status = "Fasting blood sugar is low."
        elif fasting_blood_sugar <= 110:
            fasting_sugar_status = "Fasting blood sugar is normal."
        else:
            fasting_sugar_status = "Fasting blood sugar is high."
    elif age <= 18:
        if fasting_blood_sugar < 70:
            fasting_sugar_status = "Fasting blood sugar is low."
        elif fasting_blood_sugar <= 140:
            fasting_sugar_status = "Fasting blood sugar is normal."
        else:
            fasting_sugar_status = "Fasting blood sugar is high."
    else:
        if fasting_blood_sugar < 70:
            fasting_sugar_status = "Fasting blood sugar is low."
        elif fasting_blood_sugar <= 130:
            fasting_sugar_status = "Fasting blood sugar is normal."
        else:
            fasting_sugar_status = "Fasting blood sugar is high."
    st.markdown(f"**Fasting Blood Sugar:** {fasting_sugar_status}")

    # Random Blood Sugar Check
    random_sugar_status = ""
    if age <= 3:
        if random_blood_sugar < 60:
            random_sugar_status = "Random blood sugar is low."
        elif random_blood_sugar <= 180:
            random_sugar_status = "Random blood sugar is normal."
        else:
            random_sugar_status = "Random blood sugar is high."
    elif age <= 18:
        if random_blood_sugar < 70:
            random_sugar_status = "Random blood sugar is low."
        elif random_blood_sugar <= 180:
            random_sugar_status = "Random blood sugar is normal."
        else:
            random_sugar_status = "Random blood sugar is high."
    else:
        if random_blood_sugar < 70:
            random_sugar_status = "Random blood sugar is low."
        elif random_blood_sugar <= 180:
            random_sugar_status = "Random blood sugar is normal."
        else:
            random_sugar_status = "Random blood sugar is high."
    st.markdown(f"**Random Blood Sugar:** {random_sugar_status}")

    # Heart Rate Check
    heart_rate_status = ""
    if 1 <= age <= 3:
        if heart_rate < 80:
            heart_rate_status = "Heart rate is low."
        elif heart_rate < 130:
            heart_rate_status = "Heart rate is normal."
        else:
            heart_rate_status = "Heart rate is high."
    elif 4 <= age <= 5:
        if heart_rate < 80:
            heart_rate_status = "Heart rate is low."
        elif heart_rate < 110:
            heart_rate_status = "Heart rate is normal."
        else:
            heart_rate_status = "Heart rate is high."
    elif 6 <= age <= 12:
        if heart_rate < 70:
            heart_rate_status = "Heart rate is low."
        elif heart_rate < 100:
            heart_rate_status = "Heart rate is normal."
        else:
            heart_rate_status = "Heart rate is high."
    elif age >= 13:
        if heart_rate < 60:
            heart_rate_status = "Heart rate is low."
        elif heart_rate < 100:
            heart_rate_status = "Heart rate is normal."
        else:
            heart_rate_status = "Heart rate is high."
    st.markdown(f"**Heart Rate:** {heart_rate_status}")

    # Temperature Check
    temperature_status = ""
    if 0 <= age <= 1:
        if temperature < 36.5:
            temperature_status = "Body temperature is low."
        elif temperature < 37.7:
            temperature_status = "Body temperature is normal."
        else:
            temperature_status = "Body temperature is high."
    elif age <= 10:
        if temperature < 36.5:
            temperature_status = "Body temperature is low."
        elif temperature < 37.0:
            temperature_status = "Body temperature is normal."
        else:
            temperature_status = "Body temperature is high."
    elif age <= 65:
        if temperature < 36.2:
            temperature_status = "Body temperature is low."
        elif temperature < 37.0:
            temperature_status = "Body temperature is normal."
        else:
            temperature_status = "Body temperature is high."
    else:
        if temperature < 36.0:
            temperature_status = "Body temperature is low."
        elif temperature < 36.8:
            temperature_status = "Body temperature is normal."
        else:
            temperature_status = "Body temperature is high."
    st.markdown(f"**Temperature:** {temperature_status}")

    st.markdown("---")
    st.info(f"Basic assessment complete for **{name}**.")
st.write("The first website of my life by : Yasa Sardar ")
mn=st.cache("who are you ?") 

