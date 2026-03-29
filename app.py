import streamlit as st

st.set_page_config(page_title="Healthcare Assistant", page_icon="🩺")

st.title("🩺 AI Healthcare Monitoring Assistant")

# Sidebar
st.sidebar.title("🧭 Navigation")
menu = st.sidebar.selectbox("Select Option", ["Home", "Medication", "Chatbot"])

# ---------------- HOME ----------------
if menu == "Home":
    st.header("🏠 Welcome")

    st.write("💙 Get Well Soon! Your health matters to us.")

    # Image
    st.image("https://cdn.pixabay.com/photo/2020/04/10/18/07/doctor-5025288_1280.png", width=300)

    st.info("This app helps you track medicines and get basic health suggestions.")

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
            if med_name != "":
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
    st.header("🤖 Health Chatbot")

    user_input = st.text_input("Ask your health question")

    if user_input:
        user_input = user_input.lower()

        # Fever
        if "fever" in user_input or "temperature" in user_input:
            st.success("🌡️ You may have fever.")
            st.write("👉 Drink plenty of water 💧")
            st.write("👉 Take rest 🛌")

        # Headache
        elif "headache" in user_input:
            st.success("💆 Headache detected.")
            st.write("👉 Take rest 😴")
            st.write("👉 Avoid screens 📱")

        # Cold
        elif "cold" in user_input:
            st.success("🤧 Cold symptoms.")
            st.write("👉 Warm fluids ☕")
            st.write("👉 Steam inhalation ♨️")

        # Cough
        elif "cough" in user_input:
            st.success("😷 Cough detected.")
            st.write("👉 Honey + warm water 🍯")

        # Throat pain
        elif "throat" in user_input:
            st.success("😖 Throat pain.")
            st.write("👉 Gargle warm salt water 🧂")
            st.write("👉 Drink warm liquids ☕")

        # Teeth pain
        elif "teeth" in user_input or "tooth" in user_input:
            st.success("🦷 Tooth pain.")
            st.write("👉 Rinse with warm salt water")
            st.write("👉 Avoid very cold or hot food")

        # Muscle pain
        elif "muscle" in user_input:
            st.success("💪 Muscle pain.")
            st.write("👉 Take rest 🛌")
            st.write("👉 Apply warm compress 🔥")

        # Stomach
        elif "stomach" in user_input:
            st.success("🍲 Stomach issue.")
            st.write("👉 Eat light food 🍚")
            st.write("👉 Drink water 💧")

        # General
        elif "not feeling well" in user_input:
            st.info("😷 You may feel unwell.")
            st.write("👉 Take rest 🛌")
            st.write("👉 Stay hydrated 💧")

        else:
            st.warning("⚠️ Please consult a doctor for proper advice.")

        st.info("💙 Get well soon! Take care.")