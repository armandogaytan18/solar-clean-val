import streamlit as st
import streamlit.components.v1 as components # Necesario para Calendly
import pandas as pd
from datetime import datetime
import os

# Configuración profesional
st.set_page_config(page_title="Solar Clean Pro | Citas", page_icon="📅", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; background-color: #007bff; color: white; border-radius: 8px; }
    h1 { color: #1e3a8a; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.title("☀️ Agenda tu Inspección Solar en Minutos")
st.write("Selecciona el día y la hora que mejor te convenga para que visitemos tu propiedad en **McMinnville** o alrededores.")

st.divider()

# --- SECCIÓN DE CALENDLY ---
col_cal, col_info = st.columns([2, 1])

with col_cal:
    st.markdown("### 📅 Calendario de Disponibilidad")
    
    # --- INSTRUCCIÓN PARA EL USUARIO ---
    # Reemplaza 'TU_USUARIO' por tu nombre de usuario real de Calendly
    # Si aún no tienes uno, regístrate en Calendly.com (es gratis)
    calendly_url = "https://calendly.com/TU_USUARIO/30min" 
    
    # Incrustar Calendly usando HTML/Iframe
    components.html(
        f"""
        <div class="calendly-inline-widget" data-url="{calendly_url}" style="min-width:320px;height:630px;"></div>
        <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
        """,
        height=650,
    )

with col_info:
    st.markdown("### 💡 ¿Qué pasará después?")
    st.info("""
    1. **Confirmación:** Recibirás un correo con la confirmación de la cita.
    2. **Visita:** Llegaremos puntuales para evaluar tus paneles.
    3. **Cotización:** Te entregaremos un presupuesto exacto y un plan de mejora de eficiencia.
    """)
    
    st.warning("⚠️ **¿No encuentras horario?** Déjanos tus datos abajo y nosotros te llamamos.")

st.divider()

# --- FORMULARIO DE RESPALDO (LEADS) ---
st.markdown("### 📧 O si prefieres, nosotros te contactamos")
with st.form("backup_form"):
    c1, c2 = st.columns(2)
    with c1:
        nombre = st.text_input("Nombre")
        tel = st.text_input("Teléfono")
    with c2:
        email = st.text_input("Email")
        zip_c = st.text_input("Zip Code", value="97128")
    
    comentarios = st.text_area("Cuéntanos sobre tu instalación")
    submit = st.form_submit_button("Solicitar que me llamen")
    
    if submit:
        if nombre and (tel or email):
            # Guardado local
            nuevo_lead = {"Fecha": datetime.now(), "Nombre": nombre, "Tel": tel, "Email": email}
            df = pd.DataFrame([nuevo_lead])
            df.to_csv("leads_emergencia.csv", mode='a', header=not os.path.exists("leads_emergencia.csv"), index=False)
            st.success("¡Perfecto! Te llamaremos pronto.")
        else:
            st.error("Por favor llena los campos de contacto.")

# Footer
st.caption("© 2026 Solar Clean Pro | Agendamiento Automatizado")
