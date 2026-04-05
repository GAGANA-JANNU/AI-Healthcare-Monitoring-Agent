import streamlit as st

# Page setup
st.set_page_config(page_title="Healthcare Assistant", page_icon="🩺")

st.title("🩺 AI Healthcare Monitoring Assistant")

# Sidebar
st.sidebar.title("🧭 Navigation")
menu = st.sidebar.selectbox(
    "Select Option",
    ["Home", "Medication", "Chatbot", "Health Check"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.header("🏠 Welcome")

    st.image(
        "https://cdn.pixabay.com/photo/2020/04/10/18/07/doctor-5025288_1280.png",
        width=300
    )

    st.success("💙 Get Well Soon! Stay healthy and safe.")
    st.info("This app helps track medicines, check health, and get basic advice.")
    st.warning("⚠️ Disclaimer: This is not a medical diagnosis tool.")

# ---------------- MEDICATION ----------------
elif menu == "Medication":
    st.header("💊 Medication Tracker")

    if "med_list" not in st.session_state:
        st.session_state.med_list = []

    med_name = st.text_input("💊 Medicine Name")
    time = st.time_input("⏰ Time")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Medicine"):
            if med_name:
                st.session_state.med_list.append((med_name, time))
                st.success(f"{med_name} added at {time}")
            else:
                st.warning("Enter medicine name")

    with col2:
        if st.button("🗑️ Clear All"):
            st.session_state.med_list = []
            st.warning("All medicines cleared")

    st.subheader("📋 Your Medicines")

    if st.session_state.med_list:
        for i, med in enumerate(st.session_state.med_list):
            st.write(f"{i+1}. 💊 {med[0]} at ⏰ {med[1]}")
    else:
        st.info("No medicines added yet")

# ---------------- CHATBOT ----------------
elif menu == "Chatbot":
    st.header("🤖 Smart Health Chatbot")

    user_input = st.text_input("Describe your symptoms")

    if user_input:
        user_input = user_input.lower()
        severity = "Low"

        if "fever" in user_input:
            severity = "Medium"
            st.success("🌡️ Fever detected")
            st.write("👉 Drink water and take rest")

        elif "chest pain" in user_input:
            severity = "High"
            st.error("🚨 Possible serious condition!")
            st.write("👉 Seek immediate medical help")

        elif "headache" in user_input:
            st.success("💆 Headache")
            st.write("👉 Rest and stay hydrated")

        elif "throat" in user_input:
            st.success("😖 Throat pain")
            st.write("👉 Warm salt water gargle")

        elif "tooth" in user_input:
            st.success("🦷 Tooth pain")
            st.write("👉 Avoid cold food and visit dentist if severe")

        elif "muscle" in user_input:
            st.success("💪 Muscle pain")
            st.write("👉 Rest and apply heat")

        elif "stomach" in user_input:
            severity = "Medium"
            st.success("🍲 Stomach issue")
            st.write("👉 Eat light food and stay hydrated")

        elif "bmi" in user_input:
            st.info("📊 Please go to 'Health Check' section to calculate BMI.")

        else:
            st.warning("⚠️ Unknown condition")
            st.write("👉 Please consult a doctor")

        st.info(f"🧠 Severity Level: {severity}")
        st.info("💙 Get well soon! Take care.")

# ---------------- HEALTH CHECK (BMI) ----------------
elif menu == "Health Check":
    st.header("📊 BMI Health Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=0.0)
    height = st.number_input("Enter your height (meters)", min_value=0.0)

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height ** 2)
            st.success(f"Your BMI is: {round(bmi, 2)}")

            if bmi < 18.5:
                st.warning("⚠️ Underweight")
            elif 18.5 <= bmi < 25:
                st.success("✅ Normal weight")
            else:
                st.error("⚠️ Overweight")
        else:
            st.warning("Enter valid height")