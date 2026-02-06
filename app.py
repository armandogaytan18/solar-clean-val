import streamlit as st 
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="Solar Clean McMinnville", page_icon="☀️")

# Encabezado con gancho comercial
st.title("☀️ Solar Clean McMinnville")
st.subheader("¡No dejes que la lluvia de Oregon ensucie tus ahorros!")

st.markdown("""
¿Sabías que la acumulación de polen y minerales puede reducir la eficiencia de tus paneles hasta en un **30%**? 
La lluvia no es suficiente para limpiarlos. 
             
**Ofrecemos:**
* Limpieza técnica con agua desionizada (sin manchas).
* Inspección visual de micro-fisuras.
* Reporte de eficiencia post-limpieza.
""")

st.divider()

# Formulario de captura
st.write("### Reserva una inspección gratuita en Yamhill County")
with st.form("solicitud_cliente"):
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono de contacto")
    zip_code = st.selectbox("Código Postal", ["97128", "97111", "97132", "97115", "97116", "Otro"])
    
    boton_envio = st.form_submit_button("Solicitar cotización gratuita")

    if boton_envio:
        if nombre and (email or telefono):
            # Preparar los datos
            nuevo_lead = {
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Nombre": nombre,
                "Email": email,
                "Telefono": telefono,
                "Zip": zip_code
            }
            df = pd.DataFrame([nuevo_lead])
            
            # Revisar si el archivo existe para poner o no el encabezado
            nombre_archivo = "interesados.csv"
            existe = os.path.exists(nombre_archivo)
            
            # Guardar en el CSV
            df.to_csv(nombre_archivo, mode='a', header=not existe, index=False)
            
            st.success(f"¡Excelente {nombre}! Hemos recibido tu solicitud. Te contactaremos en menos de 24 horas.")
            st.balloons()
        else:
            st.error("Por favor, introduce al menos tu nombre y un medio de contacto (Email o Teléfono).")

# Footer informativo
st.info("📍 Servicio local en McMinnville y alrededores. Garantía de eficiencia.")


if st.sidebar.checkbox("Ver base de datos (Solo Administrador)"):
    if os.path.exists("interesados.csv"):
        data = pd.read_csv("interesados.csv")
        st.sidebar.write(data)
        st.sidebar.download_button("Descargar Excel/CSV", data.to_csv(index=False), "leads_solar.csv")
