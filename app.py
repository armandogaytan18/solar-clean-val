import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Solar Panel Clean McMinnville", page_icon="☀️", layout="centered")

# Estilos personalizados para diseño y botón verde
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
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    h1 { color: #1e3a8a; text-align: center; }
    .vision-section {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffcc00;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO Y GANCHO COMERCIAL ---
st.title("☀️ Solar Panel Clean McMinnville 🏠")
st.subheader("¡No dejes que la lluvia de Oregon ensucie tus ahorros!")

st.markdown("""
At **Solar Panel Clean McMinnville**, we offer premium solar panel cleaning services that will help you maximize your return on investment. 
Our team of experts use a specially engineered process that safely and effectively removes ash, dirt, grime, and other debris from your panels.

¿Sabías que la acumulación de polen y minerales puede reducir la eficiencia de tus paneles hasta en un **30%**? 
La lluvia no es suficiente para limpiarlos.
""")

# --- BENEFICIOS (COLUMNAS) ---
st.info("**Ofrecemos:**\n"
        "* ✅ Limpieza técnica con agua desionizada (Spot-free).\n"
        "* ✅ Inspección visual de micro-fisuras.\n"
        "* ✅ Reporte de eficiencia post-limpieza.")

# --- SECCIÓN DE VISIÓN ---
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

# --- INTERFAZ DE AGENDAMIENTO ---
st.markdown("### 📅 Agenda tu inspección técnica hoy")
st.write("Completa los datos para reservar tu espacio en nuestro calendario.")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 1. Elige Fecha y Hora")
        fecha_cita = st.date_input("Día de la visita", min_value=datetime.now().date())
        horas = ["08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM"]
        hora_cita = st.selectbox("Hora disponible", horas)

    with col2:
        st.markdown("##### 2. Información de Contacto")
        nombre = st.text_input("Nombre completo")
        telefono = st.text_input("Teléfono de contacto")
        email = st.text_input("Email")

    direccion = st.text_input("Dirección de la propiedad (McMinnville / Yamhill County)")
    notas = st.text_area("Notas adicionales o tipo de instalación")

    # --- BOTÓN DE AGENDAR (VERDE) ---
    if st.button("✅ AGENDAR MI CITA AHORA"):
        if nombre and telefono and direccion:
            # Crear el registro
            nuevo_registro = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Fecha_Cita": str(fecha_cita),
                "Hora": hora_cita,
                "Cliente": nombre,
                "Tel": telefono,
                "Email": email,
                "Direccion": direccion,
                "Notas": notas
            }
            
            # Guardar en base de datos local
            archivo = "agenda_solar_completa.csv"
            existe = os.path.exists(archivo)
            pd.DataFrame([nuevo_registro]).to_csv(archivo, mode='a', header=not existe, index=False)
            
            st.success(f"¡Excelente {nombre}! Tu cita ha sido agendada para el {fecha_cita} a las {hora_cita}.")
            st.balloons()
            st.warning("Te enviaremos un mensaje de confirmación a tu teléfono en breve.")
        else:
            st.error("⚠️ Por favor completa los campos obligatorios (Nombre, Teléfono y Dirección) para agendar.")

# --- SECCIÓN ADMINISTRADOR ---
st.divider()
with st.expander("🔑 Acceso Administrador"):
    if os.path.exists("agenda_solar_completa.csv"):
        datos = pd.read_csv("agenda_solar_completa.csv")
        st.write("Citas registradas:")
        st.dataframe(datos)
        st.download_button("Descargar Base de Datos", datos.to_csv(index=False), "leads_solar.csv")
    else:
        st.write("Aún no hay registros de clientes.")

# Footer
st.caption("© 2026 Solar Panel Clean McMinnville | Maximize your Energy Production")
