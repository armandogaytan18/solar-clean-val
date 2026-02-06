import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os

# Configuración de la página
st.set_page_config(page_title="Solar Clean Pro | Agenda", page_icon="📅", layout="centered")

# Estilos personalizados (CSS) para el botón verde y diseño
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #28a745 !important;
        color: white !important;
        font-weight: bold !important;
        padding: 0.75rem !important;
        border-radius: 10px !important;
        border: none !important;
        font-size: 1.2rem !important;
    }
    .stButton>button:hover {
        background-color: #218838 !important;
        border: none !important;
    }
    h1 { color: #1e3a8a; text-align: center; }
    .status-box { border: 1px solid #ddd; padding: 20px; border-radius: 10px; background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- TÍTULO Y EXPLICACIÓN ---
st.title("☀️ Sistema de Agendamiento Solar")
st.write("Selecciona el momento ideal para tu inspección técnica en McMinnville.")

st.divider()

# --- INTERFAZ DE AGENDAMIENTO ---
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1. Fecha y Hora")
        # Selección de Fecha (Día, Mes, Año)
        # No permitimos fechas pasadas (min_value=today)
        fecha_cita = st.date_input("Selecciona el día", min_value=datetime.now().date())
        
        # Selección de Hora
        horas_disponibles = [
            "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", 
            "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"
        ]
        hora_cita = st.selectbox("Selecciona la hora", horas_disponibles)

    with col2:
        st.markdown("### 2. Tus Datos")
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono (para confirmar)")
        email = st.text_input("Correo electrónico")

    # Selección de servicio extra
    st.markdown("---")
    direccion = st.text_input("Dirección exacta en Yamhill County")
    notas = st.text_area("Notas adicionales (ej: número de paneles, acceso al techo)")

    # --- BOTÓN DE AGENDAR (VERDE) ---
    if st.button("✅ AGENDAR CITA AHORA"):
        if nombre and telefono and direccion:
            # Creamos el registro
            nueva_cita = {
                "ID_Orden": datetime.now().strftime("%y%m%d%H%M%S"),
                "Fecha_Registro": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Fecha_Cita": fecha_cita.strftime("%d/%m/%Y"),
                "Hora_Cita": hora_cita,
                "Cliente": nombre,
                "Telefono": telefono,
                "Email": email,
                "Direccion": direccion,
                "Notas": notas,
                "Estado": "Pendiente de Confirmación"
            }
            
            # Guardar en la base de datos (CSV)
            df = pd.DataFrame([nueva_cita])
            archivo = "agenda_solar.csv"
            existe = os.path.exists(archivo)
            df.to_csv(archivo, mode='a', header=not existe, index=False)
            
            # Mensaje de éxito
            st.success(f"¡Cita agendada con éxito para el {fecha_cita.strftime('%d de
