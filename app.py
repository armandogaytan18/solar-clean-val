import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Configuración de la página
st.set_page_config(page_title="Solar Panel Clean McMinnville", page_icon="☀️", layout="centered")

# 2. Traductor de Google
st.markdown("""
    <div id="google_translate_element" style="text-align:right; padding:10px;"></div>
    <script type="text/javascript">
        function googleTranslateElementInit() {
            new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
        }
    </script>
    <script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
""", unsafe_allow_html=True)

# 3. Estilos Personalizados
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #28a745 !important;
        color: white !important;
        font-weight: bold !important;
        padding: 0.8rem !important;
        border-radius: 12px !important;
        border: none !important;
        font-size: 1.3rem !important;
    }
    h1, h3 { color: #1e3a8a; }
    .vision-section {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Contenido Principal
st.title("☀️ Solar Panel Clean McMinnville 🏠")
st.subheader("Don't let the Oregon rain wash away your savings!")

st.markdown("""
At **Solar Panel Clean McMinnville**, we offer premium solar panel cleaning services that will help you maximize your return on investment. 
Our team of experts uses a specially engineered process that safely and effectively removes ash, dirt, grime, and other debris from your panels.
""")

st.info("**What we offer:**\n"
        "* ✅ Technical cleaning with deionized water (Spot-free).\n"
        "* ✅ Visual inspection for micro-cracks.\n"
        "* ✅ Post-cleaning efficiency report.")

st.markdown('<div class="vision-section">', unsafe_allow_html=True)
st.markdown("""
**Our Vision:**
Cleaning your solar panels is essential to maintain their efficiency and maximize energy production. 
Dust, dirt, and debris can accumulate over time, reducing their ability to capture sunlight. 
Regular cleaning ensures peak performance, allowing you to generate more electricity and ultimately **save money** on your energy bills. 
Additionally, clean panels have a longer lifespan, minimizing maintenance costs for years to come.
""")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# 5. Interfaz de Agendamiento
st.markdown("### 📅 Schedule Your Technical Inspection Today")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 1. Choose Date and Time")
        fecha_cita = st.date_input("Visit Date", min_value=datetime.now().date())
        # Definición limpia de la lista de horas
        horas_lista = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"]
        hora_cita = st.selectbox("Available Time", options=horas_lista)

    with col2:
        st.markdown("##### 2. Contact Information")
        nombre = st.text_input("Full Name")
        telefono = st.text_input("Phone Number")
        email = st.text_input("Email Address")

    direccion = st.text_input("Property Address (McMinnville / Yamhill County)")
    notas = st.text_area("Additional notes or installation type")

    # 6. Lógica del Botón de Agendar
    if st.button("✅ SCHEDULE MY APPOINTMENT NOW"):
        if nombre and telefono and direccion:
            # Diccionario de datos
            nuevo_registro = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Appt_Date": str(fecha_cita),
                "Time": hora_cita,
                "Customer": nombre,
                "Phone": telefono,
                "Email": email,
                "Address": direccion,
                "Notes": notas
            }
            
            # Guardado en CSV
            archivo = "agenda_solar_completa.csv"
            existe_archivo = os.path.exists(archivo)
            df_nuevo = pd.DataFrame([nuevo_registro])
            df_nuevo.to_csv(archivo, mode='a', header=not existe_archivo, index=False)
            
            st.success(f"Excellent {nombre}! Your appointment is scheduled for {fecha_cita} at {hora_cita}.")
            st.balloons()
            st.warning("We will send a confirmation message to your phone shortly.")
        else:
            st.error("⚠️ Please complete the required fields (Name, Phone, and Address) to schedule.")

# 7. Sección Administrador
st.divider()
with st.expander("🔑 Admin Access"):
    if os.path.exists("agenda_solar_completa.csv"):
        datos_csv = pd.read_csv("agenda_solar_completa.csv")
        st.write("Registered Appointments:")
        st.dataframe(datos_csv)
        st.download_button("Download Database", datos_csv.to_csv(index=False), "leads_solar.csv")
    else:
        st.write("No customer records yet.")

st.caption("© 2026 Solar Panel Clean McMinnville | Maximize your Energy Production")
