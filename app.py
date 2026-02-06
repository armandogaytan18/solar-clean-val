import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Solar Clean Pro | Agenda", page_icon="📅", layout="centered")

# Estilos para el botón verde y diseño
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
    h1 { color: #1e3a8a; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("☀️ Sistema de Agendamiento Solar")
st.write("Selecciona el momento ideal para tu inspección técnica en **McMinnville**.")

st.divider()

# --- INTERFAZ DE AGENDAMIENTO ---
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1. Fecha y Hora")
        fecha_cita = st.date_input("Selecciona el día", min_value=datetime.now().date())
        horas = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"]
        hora_cita = st.selectbox("Selecciona la hora", horas)

    with col2:
        st.markdown("### 2. Tus Datos")
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono")
        email = st.text_input("Correo electrónico")

    st.markdown("---")
    direccion = st.text_input("Dirección exacta en Yamhill County")
    notas = st.text_area("Notas adicionales (opcional)")

    # --- BOTÓN DE AGENDAR (VERDE) ---
    if st.button("✅ AGENDAR CITA AHORA"):
        if nombre and telefono and direccion:
            # Creamos el registro
            nueva_cita = {
                "Fecha_Registro": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Fecha_Cita": str(fecha_cita),
                "Hora_Cita": hora_cita,
                "Cliente": nombre,
                "Telefono": telefono,
                "Email": email,
                "Direccion": direccion,
                "Notas": notas
            }
            
            # Guardar en CSV
            df = pd.DataFrame([nueva_cita])
            archivo = "agenda_solar.csv"
            existe = os.path.exists(archivo)
            df.to_csv(archivo, mode='a', header=not existe, index=False)
            
            # Mensaje de éxito simplificado para evitar errores de comillas
            st.success(f"¡Cita agendada para el {fecha_cita} a las {hora_cita}!")
            st.balloons()
            st.info(f"Confirmaremos al teléfono: {telefono}")
        else:
            st.error("⚠️ Por favor completa: Nombre, Teléfono y Dirección.")

# --- SECCIÓN ADMINISTRADOR ---
st.divider()
with st.expander("🔐 Ver Agenda (Solo Dueño)"):
    if os.path.exists("agenda_solar.csv"):
        datos = pd.read_csv("agenda_solar.csv")
        st.dataframe(datos)
        st.download_button("Descargar Excel", datos.to_csv(index=False), "agenda.csv")
    else:
        st.write("No hay citas registradas aún.")
